from django.forms import fields, widgets
#from Ecommerce.userApp import models
from django import forms #its Model Forms in django
from django.contrib.auth import password_validation 
from django.contrib.auth.forms import UserCreationForm # its Buildin userCreatin form  which help to craete and validate UserForms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm ,  UsernameField ,PasswordChangeForm
from django.utils.translation import gettext , gettext_lazy as _
from django.contrib.auth import password_validation #password_validation used in MyPasswordChangeForm class
from django.contrib.auth.forms import PasswordResetForm # PasswordResetForm used in reset password through email field
from django.contrib.auth.forms import SetPasswordForm # SetPasswordForm used to reset Forgoten Password 
from .models import Customer



class CustomerRegistrationForm(UserCreationForm):#Inheriting UserCreationForm Class
  password1 = forms.CharField(label ='password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
                                                        
  password2 = forms.CharField(label ='Confirm password(again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
  email = forms.CharField( required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
                                       #here required = True is used as Required field validator
  class Meta:  
      model = User                                      
      fields = ['username','email','password1','password2']
      labels = {'email':'Email'} 
      widgets={'username': forms.TextInput(attrs={'class':'form-control'})}
                                                        

class LoginForm(AuthenticationForm):
  username = UsernameField(widget=forms.TextInput(attrs=
  {'autofocus':True, 'class':'form-control'}))
  password = forms.CharField(label=_("password"), strip=False,
  widget=forms.PasswordInput(attrs= {'autocomplete':'current-password','class':'form-control' }))



class MyPasswordChangeForm(PasswordChangeForm):
  old_password = forms.CharField(label=_("old Password"), strip=False,widget=forms.PasswordInput(attrs=
  { 'autocomplet':'current-password','autofocus':True,'class':'form-control'}))

  new_password1 = forms.CharField(label=_("New Password"), strip=False,widget=forms.PasswordInput(attrs=
  { 'autocomplet':'new-password','autofocus':True,'class':'form-control'}),help_text=password_validation.
  password_validators_help_text_html)

  new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False,widget=forms.PasswordInput(attrs=
  { 'autocomplet':'current-password','autofocus':True,'class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
  email = forms.EmailField(label=_("Email"),max_length=254, 
  widget=forms.EmailInput(attrs={'autocomplete':'email', 'class':'form-control'}))

  # inbuild class PasswordResetForm  only take email field input to send link to reset password


class MyForgotenPassForm(SetPasswordForm):
  new_password1 = forms.CharField(label=_("New Password"), strip=False,widget=forms.PasswordInput(attrs=
      { 'autocomplet':'new-password','class':'form-control'}),help_text=password_validation.
       password_validators_help_text_html)

  new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False,widget=forms.PasswordInput(attrs=
      { 'autocomplet':'current-password','class':'form-control'}))

# this class will inherite from inbuild SetPasswordForm . it will take two input field i.e (new paasword , confirm password

class CustomerProfileForm(forms.ModelForm):
  class Meta:
    model=Customer
    fields = ['name','locality','city','state','zipcode']
    widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),
    'locality':forms.TextInput(attrs={'class':'form-control'}),
    'city':forms.TextInput(attrs={'class':'form-control'}),
    'state':forms.Select(attrs={'class':'form-control'})
    ,'zipcode':forms.TextInput(attrs={'class':'form-control'})}