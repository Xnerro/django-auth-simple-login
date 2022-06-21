from django.forms import ModelForm
from .models import Account

class RegisterForm(ModelForm):
    class Meta:
        model = Account
        fields = ['fname', 'lname', 'username', 'email', 'password']