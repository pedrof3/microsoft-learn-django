from django.db import models
from django.urls import reverse

# Create your models here.

class Shelter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Dog(models.Model):
    shelter = models.ForeignKey(Shelter, on_delete=models.PROTECT)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    intake_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('dog_detail', kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
    