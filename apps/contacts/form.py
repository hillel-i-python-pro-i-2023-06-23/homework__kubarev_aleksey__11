from django import forms

from apps.contacts.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
