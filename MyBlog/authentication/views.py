from django.shortcuts import render, redirect
from django.views.generic.base import TemplateResponseMixin
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from authentication.forms import RegistrationForm
from django.contrib.auth import get_user_model


User = get_user_model()

class RegisterUserView(View, TemplateResponseMixin):

    Reg_form = RegistrationForm
    template_name = "signup.html"

    def get(self, request, *args, **kwargs):
        return self.render_to_response({'form' : self.Reg_form()})

    
    def post(self, request,*args,**kwargs):
        user_email = request.POST.get('email')

        form = self.Reg_form(request.POST)

        if form.is_valid() is False:
            return render_to_response({'form': form})

        user = form.save()
        return redirect(reverse('login'))


class UserLoginView(LoginView):
    template_name = 'login.html'