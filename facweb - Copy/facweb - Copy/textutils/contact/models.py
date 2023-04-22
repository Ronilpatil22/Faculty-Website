from django.db import models
from datetime import date
# Create your models here.
class contacts(models.Model):
    BIG_TEXT_LEFT = models.CharField(max_length=2000,blank=True)
    SMALL_TEXT = models.CharField(max_length=2000,blank=True)
    ADDRESS = models.CharField(max_length=2000,blank=True)
    PHONE = models.CharField(max_length=2000,blank=True)
    EMAIL = models.EmailField(blank=True)
    WEBSITE = models.URLField(blank=True)
    FORM_BIG_TEXT = models.CharField(max_length=2000,blank=True)
    FORM_SUBMIT_MESSAGE_TEXT = models.CharField(max_length=2000,blank=True)


class getintouch_details(models.Model):
    Name = models.CharField(max_length=2000,blank=True)
    Email = models.EmailField(max_length=2000)
    Subject = models.CharField(max_length=10000,default=Name)
    Message = models.CharField(max_length=10000000)

    def __str__(self):
        return self.Name