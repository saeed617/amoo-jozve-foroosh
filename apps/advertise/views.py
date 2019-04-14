from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView
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


class AddAdvertise(FormView):
    template_name = 'advertise/new_advertise.html'
    form_class = AdvertiseForm
    success_url = reverse_lazy('advertise:list')

    def form_valid(self, form):
        advertise = form.save(commit=False)
        advertise.user = User.objects.first()
        advertise.state = Advertise.PENDING
        advertise.save()
        messages.add_message(self.request, messages.SUCCESS, _('Advertise added successfully.'))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, _('Please correct the following errors.'))
        return super().form_invalid(form)
