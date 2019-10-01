from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length = 150)
    description = models.TextField()
    opening_time = models.TextField()
    closing_time =models.TextField()

    def __str__(self):
        return self.name