from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Iha, Rent
from django.forms import DateInput



#default User Creation Form
# Django.contrib.auth kütüphanesinde default olarak user modelini oluşturuyor.
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User #creating user model
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2'] #6 tane input var

# iha oluşturmak için form
class IhaForm(forms.ModelForm):
    class Meta:
        model = Iha
        fields = '__all__'

# iha kiralamak için gereken form
class RentIhaForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ['iha', 'start_date', 'end_date']
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'}),
        }