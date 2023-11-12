from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField

class CustomUserCreationForm(UserCreationForm):
    captcha = CaptchaField(label='Введите текст с картинки', error_messages={'invalid':'Неправильный текст'})
    class Meta: 
        model = CustomUser
        fields = ('username', 'password1', 'password2','captcha')
    
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
        
# class UpdateUserProfileForm(ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ('username','password','bio','avatar')