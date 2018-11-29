from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name',
                  'email', 'phone_number', 'message']
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name',
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name',
            }),
            'phone_number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number (optional)',
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }),
            'message': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message',
            }),
        }
