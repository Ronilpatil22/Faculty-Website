from django.db import models

# Create your models here.
class Navbar(models.Model):
    SECTION_NAME = models.CharField(max_length=2000,blank=True)
    SECTION_LINK = models.CharField(max_length=200,blank=True,choices=[("index","Home Page"),("mywork","My Work Section"),("aboutme","About Me Section"),("contact","Contact Me Section"),("research","Research Group Section"),("students","Students Portal Section"),("discussion","Discussion Section"),("creators","Creators Section")])
    
    def __str__(self):
        return self.SECTION_NAME

class Navbar_icon(models.Model):
    ICON = models.ImageField(upload_to='images/navbar',blank=True)
    ICON_LINK = models.CharField(max_length=200,blank=True,choices=[("index","Home Page"),("mywork","My Work Section"),("aboutme","About Me Section"),("contact","Contact Me Section"),("research","Research Group Section"),("students","Students Portal Section"),("discussion","Discussion Section"),("creators","Creators Section")])

class socialmediabar(models.Model):
    Name = models.CharField(max_length=2000)
    Link = models.URLField()
    
    def __str__(self):
        return self.Name

class socialmediabarmessage(models.Model):
    Text = models.CharField(max_length=2000)

