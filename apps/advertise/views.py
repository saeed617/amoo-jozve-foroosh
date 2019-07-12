from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, get_object_or_404

from apps.advertise.forms import CommentForm
from apps.advertise.models import Province, County, University, Comment, Rate
from apps.utils.decorators import require_ajax
from .models import Advertise
from .forms import AdvertiseForm, AdvertiseImageFormSet


class AdvertiseListView(ListView):
    template_name = 'advertise/advertise_list.html'
    paginate_by = 12

    def get_queryset(self):
        major = self.request.GET.get('major')
        university = self.request.GET.get('university')
        province = self.request.GET.get('province')
        county = self.request.GET.get('county')

        qs = Advertise.objects.all()
        if major:
            qs = qs.filter(major=major)
        if university:
            university = int(university)
            qs = qs.filter(university__id=university)
        if not county:
            if province:
                province = int(province)
                qs = qs.filter(county__province__id=province)
        if county:
            county = int(county)
            qs = qs.filter(county__id=county)
        return qs.filter(state=Advertise.PUBLISHED).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['majors'] = Advertise.MAJOR_CHOICES
        context['universities'] = University.objects.all()
        context['provinces'] = Province.objects.all()
        context['counties'] = County.objects.none()
        return context


class AdvertiseDetailView(DetailView):
    template_name = 'advertise/advertise_detail.html'
    model = Advertise

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm(None)
        context['rate'] = Rate.objects.filter(user=self.request.user, advertise=self.get_object())
        context['comments'] = Comment.objects.filter(advertise__id=self.get_object().pk).order_by('-timestamp')
        return context


def filter_cities(request):
    if request.method == "GET" and request.is_ajax():
        province = request.GET.get('province')
        if province:
            response = {}
            data = County.objects.filter(province__id=int(province))
            for county in data:
                response[county.id] = {'id': county.id, 'name': county.name}
            return JsonResponse(response)
        return JsonResponse({"message": "Invalid province"})


class AddAdvertise(LoginRequiredMixin, FormView):
    template_name = 'advertise/new_advertise.html'
    form_class = AdvertiseForm
    success_url = reverse_lazy('advertise:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['provinces'] = Province.objects.all()
        if self.request.POST:
            context['image_formset'] = AdvertiseImageFormSet(self.request.POST, self.request.FILES)
        else:
            context['image_formset'] = AdvertiseImageFormSet()
        return context

    def form_valid(self, form):
        advertise = form.save(commit=False)
        advertise.user = self.request.user
        advertise.state = Advertise.PENDING
        advertise.save()
        context = self.get_context_data()
        advertise_image_formset = context['image_formset']
        advertise_image_formset.instance = advertise
        for form in advertise_image_formset.forms:
            if form.is_valid():
                image = form.save(commit=False)
                image.advertise = advertise
                image.save()
        messages.add_message(self.request, messages.SUCCESS, _('Advertise added successfully.'))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, _('Please correct the following errors.'))
        return super().form_invalid(form)


class CommentCreateView(LoginRequiredMixin, FormView):
    form_class = CommentForm

    def get_success_url(self):
        return reverse('advertise:detail', args=(self.kwargs.get('pk'),))

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.advertise = Advertise.objects.get(pk=int(self.kwargs.get('pk')))
        comment.save()
        messages.add_message(self.request, messages.SUCCESS, _('Your comment successfully added.'))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, _('Please correct the following errors.'))
        return super().form_invalid(form)


@login_required
@require_ajax
def rating(request, advertise_id):
    advertise = get_object_or_404(Advertise, id=advertise_id)
    rate = request.POST.get('rate')
    if not Rate.objects.filter(advertise=advertise, user=request.user).exists():
        Rate.objects.create(advertise=advertise, user=request.user, rate=rate)
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'ko'})
