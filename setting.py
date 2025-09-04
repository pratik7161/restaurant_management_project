EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# For real SMIP (example with Gmail):
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.gamil.com"
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = "your_email@gmail.com"
# EMAIL_HOST_PASSWORD = "your password or app password"
+
from django import forms
class ContactForm(forms.from):
    name  = froms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)