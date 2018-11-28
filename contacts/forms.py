from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name',
                  'email', 'phone_number', 'message']
        # widgets = {
        #     'first_name': _('First Name'),
        #     'last_name': _('Last Name'),
        #     'email': _('Email'),
        #     'phone_number': _('Phone Number (optional)'),
        #     'message': _('Message'),
        # }
