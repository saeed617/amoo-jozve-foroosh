from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
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


class CartDetailView(LoginRequiredMixin, View):

    def get(self, request,  pk):
        template_name = 'carts/cart_detail.html'
        cart = get_object_or_404(Cart, id=pk)
        advertises = cart.advertises.all()
        total = sum(advertise.price for advertise in advertises)
        context = {'object': cart, 'total': total, 'advertises':advertises}
        if cart.user != self.request.user:
            raise Http404
        return render(request, template_name, context=context)
