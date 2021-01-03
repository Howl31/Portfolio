from django.db import models

# Create your models here.


class Resume(models.Model):
    pic = models.FileField(upload_to="profiles")


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " | " + self.email
