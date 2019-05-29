from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.translation import ugettext as _

from .tokens import profile_activation_token
from .forms import AuthenticationForm
from .forms import UserCreationForm


class UserCreationView(CreateView):
    form_class = UserCreationForm
    template_name = 'profiles/sign_up.html'
    success_url = reverse_lazy('advertise:list')

    def form_valid(self, form):
        user = form.save()
        current_site = get_current_site(self.request)
        mail_subject = 'اکانت خود را فعال کنید.'
        message = render_to_string('profiles/activate_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
            'token': profile_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        messages.add_message(self.request, messages.SUCCESS,
                             'لطفا اقدام به فعال سازی ایمیل خود کنید.')
        return super().form_valid(form)


def authenticate_view(request):
    template_name = 'profiles/login.html'
    form = AuthenticationForm(request.POST or None)
    errors = []
    if request.method == "POST":
        if form.is_valid():
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            if not user.profile.active:
                errors.append("لطفا اقدام به فعالسازی اکانت خود کنید")
            else:
                username = user.username
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect(reverse('advertise:list'))

                else:
                    errors.append("کاربر موجود نیست")
        else:
            errors.append("اطلاعات وارد شده معتبر نیست")

    return render(request, template_name, context={'form': form, 'errors': errors})


def logout_view(request):
    logout(request)
    return redirect('advertise:list')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and profile_activation_token.check_token(user, token):
        user.profile.active = True
        user.profile.save()
        messages.add_message(request, messages.SUCCESS, _('Your account email successfully activated.'))
        return redirect(reverse('profiles:login'))

    else:
        messages.add_message(request, messages.ERROR, _('Activation link is invalid!'))
        return redirect(reverse('advertise:list'))
