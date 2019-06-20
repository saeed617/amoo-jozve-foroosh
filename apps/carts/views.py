from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.base import View

from apps.advertise.models import Advertise
from apps.carts.models import Cart


class CartCreateView(View):
    def post(self, *args, **kwargs):
        user = self.request.user
        advertise_id = self.request.POST.get('ad_id')
        advertise = Advertise.objects.get(pk=advertise_id)
        cart = user.cart
        cart.advertises.add(advertise)
        return redirect('advertise:list')


class CartRemoveView(View):
    def post(self, *args, **kwargs):
        user = self.request.user
        advertise_id = self.request.POST.get('ad_id')
        advertise = Advertise.objects.get(pk=advertise_id)
        cart = user.cart
        cart.advertises.remove(advertise)
        return redirect(reverse('carts:detail', args=(cart.id,)))


class CartDetailView(LoginRequiredMixin, DetailView):
    model = Cart
    template_name = 'carts/cart_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = sum(advertise.price for advertise in context['object'].advertises.all())
        return context
