from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from .forms import AuthenticationForm
from .forms import UserCreationForm


class UserCreationView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('profiles:login')
    template_name = 'profiles/sign_up.html'


def authenticate_view(request):
    template_name = 'profiles/login.html'
    form = AuthenticationForm(request.POST or None)
    errors = []
    if request.method == "POST":
        if form.is_valid():
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            username = user.username
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('advertise:list'))
            errors.append("کاربر موجود نیست")
        else:
            errors.append("اطلاعات وارد شده معتبر نیست")

    return render(request, template_name, context={'form': form, 'errors': errors})


def logout_view(request):
    logout(request)
    return redirect('advertise:list')
