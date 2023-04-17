from django.db import models

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
