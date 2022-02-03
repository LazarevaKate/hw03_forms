from django.contrib.auth import logout, login

from django.contrib.auth.forms import PasswordResetForm, \
    AuthenticationForm

from django.contrib.auth.views import LoginView

from django.shortcuts import redirect

from django.views.generic import CreateView

from django.urls import reverse_lazy

from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('posts:index')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/login.html'


class ResetChange():
    form_class = PasswordResetForm
    success_url = reverse_lazy('users:password_reset_confirm')
    template_name = 'users/password_reset_form.html'


def logout_user(request):
    logout(request)
    return redirect('login')



