from django.forms import ModelForm, TextInput, EmailInput
from .models import Subscriber


class SubscriberForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = ['name', 'email']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control mb-2 mr-2',
                'placeholder': 'Full Name',
            }),
            'email': EmailInput(attrs={
                'class': 'form-control mb-2 mr-2',
                'placeholder': 'Email',
            }),
        }
