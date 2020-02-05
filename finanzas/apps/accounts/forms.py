from django import forms
from django.contrib.auth.models import User
from django.contrib import auth


class LoginForm(forms.Form):
    user = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Usuario'},render_value=False)))
    password = forms.CharField(widget=forms.PasswordInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Password'},render_value=False)))

class ChangePassForm(forms.Form):
    password_actual = forms.CharField(widget=forms.PasswordInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Password Actual'},render_value=False)))
    password_nuevo = forms.CharField(widget=forms.PasswordInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nuevo Password'},render_value=False)))
    password_confirmar = forms.CharField(widget=forms.PasswordInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Repetir Nuevo Password'},render_value=False)))

class ResetPassForm(forms.Form):
    email_user = forms.CharField(widget=forms.EmailInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Em@il'},render_value=False)))
