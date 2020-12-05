from django.db import models

# Create your models here.
class AboutUs(models.Model):
    who_are_we = models.TextField()
    what_we_do = models.TextField()
    why_us = models.TextField()

    class Meta:
        verbose_name_plural = 'About Us'

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phoneNo = models.CharField(max_length=15)
    message = models.TextField()
    read = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Contact Us'
