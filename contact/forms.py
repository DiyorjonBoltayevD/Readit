from django.forms import ModelForm, TextInput, Textarea
from .models import ContactModel


class ContactForm(ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': 'inpt',
                'placeholder': 'Your name'
            }),
            'email': TextInput(attrs={
                'email': 'inpt',
                'placeholder': 'Your email',
            }),

            'subject': TextInput(attrs={
                'subject': 'inpt',
                'placeholder': 'Subject'

            }),
            'message': Textarea(attrs={
                'message': 'inpt',
                'placeholder': 'Message'
            })

        }
