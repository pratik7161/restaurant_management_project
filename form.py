from django import forms
from .models import ContactSubmission
clss ContactForm(forms.ModelForm):
   class Meta:
    model = ContactSubmission
    fields = ['name', 'email']
    
