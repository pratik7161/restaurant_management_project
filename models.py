from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    submittted_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} - {self.email}"


# for rum migration 
python manage.py makemigration
python manage.py migrate
