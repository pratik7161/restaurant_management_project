from django.db import models

# Create your models here.
class Feedback(models.Model):
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback {self.id} - {self.comments[:30]}"
