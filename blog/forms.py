from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from .models import User, Message
from django import forms
from django.forms import ModelForm, TextInput


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': TextInput(attrs={
                'class': 'inpt',
                'placeholder': 'Username',
            }),
            'password': TextInput(attrs={
                'class': 'inpt',
                'placeholder': 'Password',
                'type': 'password'
            })
        }


# class RegistrationForm(forms.Form):
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(widget=forms.PasswordInput)
#     email = forms.EmailField()
#     image = forms.ImageField(widget=forms.FileInput)

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'placeholder': 'Enter your password'
        }))
    password2 = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'placeholder': 'Confirm your password'
        }))

    class Meta:
        model = User
        fields = {
            'username',
            'first_name',
            'last_name',
            'picture',
            'bio',
            'email',
            'password1',
            'password2',
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Bio'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-mail'
            }),

        }


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message', 'parent']
        widgets = {
            'message': forms.Textarea(attrs={
                'id': 'name',
                'class': 'form-control',
            })
        }
