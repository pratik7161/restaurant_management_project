from django import forms
from .models import ContactSubmission
clss ContactForm(forms.ModelForm):
   class Meta:
    model = ContactSubmission
    fields = ['name', 'email']
    
from django.db import models
class MenuItem(models.Model):
    name = models.CharField(max_length= 100)
    description = model.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.Image.Field(upload_to='uploads/')
    def __str__(self):
        return self.name


# configure settinf.py
MEDIA_URL = '/media/'
MEDIA_PORT = BASE_DIR / 'media'
# project/urls.py
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #  ... your app urls
]
if settings.DEBUG:
    urlpattern += static(setting.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    