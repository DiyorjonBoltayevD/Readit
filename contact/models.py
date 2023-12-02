from django.db import models
from django.urls import reverse


class ContactModel(models.Model):
    name = models.CharField(max_length=221)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contact:contact', self.pk)
