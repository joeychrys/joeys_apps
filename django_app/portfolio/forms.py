from django import forms
from django.forms import ModelForm
from .models import ContactInfo

class ContactForm(ModelForm):
    class Meta:
        model = ContactInfo
        fields = ("Name", "Email", "Message")
        labels = {
            "Name": "",
            "Email": "",
            "Message": "",
        }
        widgets = {
            "Name": forms.TextInput(attrs={"class": "form-control"}),
            "Email": forms.EmailInput(attrs={"class": "form-control"}),
            "Message": forms.Textarea(attrs={"class": "form-control", 'rows':4, 'cols':15}),
        }