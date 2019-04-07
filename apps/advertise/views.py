from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Advertise


class AdvertiseListView(ListView):
    template_name = 'advertise/advertise_list.html'

    def get_queryset(self):
        return Advertise.objects.all()


class AdvertiseDetailView(DetailView):
    template_name = 'advertise/advertise_detail.html'
    model = Advertise
