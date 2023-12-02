from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView

from contact.forms import ContactForm
from contact.models import ContactModel


class ContactView(CreateView):
    model = ContactModel
    template_name = 'contact/contact.html'
    form_class = ContactForm

