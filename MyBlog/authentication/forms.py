from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

User = get_user_model()


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User

        fields = [
            'username',
            'email'
        ]

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=30)
    passowd = forms.CharField(max_length=15, validators=[validate_password])
    

    def clean_email(self):

        email = self.cleaned_data['email']

        email_obj = User.objects.filter(email=email)
        
        if email_obj.exists():
            # raise ValidationError("Email address is already exists")
            self.add_error("email", "Email address is already exists")
        
        return email


