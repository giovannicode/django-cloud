from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.views.generic import FormView

from .forms import UserCreateForm
from .models import User


from braces.views import AnonymousRequiredMixin


class UserCreateView(AnonymousRequiredMixin, CreateView):
    authenticated_redirect_url = u"/"
    model = User
    form_class = UserCreateForm

    def form_valid(self, form):
        user = form.save()
        user = authenticate(
	    username=form.cleaned_data.get('email'),
	    password=form.cleaned_data.get('password2')
        )
        login(self.request, user)
        return redirect('home')


class UserSigninView(AnonymousRequiredMixin, FormView):
    authenticated_redirect_url = u"/"
    template_name = 'users/login.html'
    form_class = AuthenticationForm
  
    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect('home')


def signout(request):
    logout(request)
    return redirect('home')
