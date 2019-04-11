from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
import json
from apps.advertise.models import Province, County
from .models import Advertise
from .forms import AdvertiseForm


class AdvertiseListView(ListView):
    template_name = 'advertise/advertise_list.html'

    def get_queryset(self):
        return Advertise.objects.all()


class AdvertiseDetailView(DetailView):
    template_name = 'advertise/advertise_detail.html'
    model = Advertise


def add_advertise(request):
    if request.method == 'POST':
        form = AdvertiseForm(request.POST)
        if form.is_valid():
            advertise = form.save(commit=False)
            advertise.user = User.objects.first()
            advertise.state = Advertise.PENDING
            advertise.save()
            messages.add_message(request, messages.SUCCESS, _('Advertise added successfully.'))
            return redirect('advertise:list')
        else:
            messages.add_message(request, messages.ERROR, _('Please correct the following errors.'))
    else:
        if request.is_ajax():
            province_id = request.GET.get("province_id")
            data = {}
            data['counties'] = json.dumps([dict(obj) for obj in County.objects.filter(province=province_id).values()])
            return JsonResponse(data)
        form = AdvertiseForm()

    options = Province.objects.all()
    return render(request, 'advertise/new_advertise.html', {'form': form, 'options': options})
