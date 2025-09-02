form django.db import models
class Restaurant(models.Model):
    name = models.CharFeild(max_length=200)
    address = models.TextField()
    def __str__(self):
        return self.name


