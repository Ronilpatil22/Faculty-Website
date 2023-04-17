from django.db import models

# Create your models here.
class introductions(models.Model):
    BIG_TEXT = models.CharField(max_length=200,blank=True)
    MEDIUM_TEXT = models.CharField(max_length=200,blank=True)
    SMALL_TEXT = models.CharField(max_length=200,blank=True)
    Profile_image = models.ImageField(upload_to='images',blank=True)
    LINK_1 = models.CharField(max_length=200,blank=True)
    LINK_1_URL = models.CharField(max_length=200,blank=True,choices=[("index","Home Page"),("mywork","My Work Section"),("aboutme","About Me Section"),("contact","Contact Me Section"),("research","Research Group Section"),("students","Students Portal Section"),("discussion","Discussion Section")])
    LINK_2 = models.CharField(max_length=200,blank=True)
    LINK_2_URL = models.CharField(max_length=200,blank=True,choices=[("index","Home Page"),("mywork","My Work Section"),("aboutme","About Me Section"),("contact","Contact Me Section"),("research","Research Group Section"),("students","Students Portal Section"),("discussion","Discussion Section")])

    
class testimonials(models.Model):
    Description = models.CharField('testimonial description',max_length=500,blank=True)
    Name = models.CharField('testimonial name',max_length=200,blank=True)
    Designation = models.CharField('testimonial designation',max_length=200,blank=True)
    Photo = models.ImageField('testimonial photo',upload_to='images/testimonials',blank=True)

    def __str__(self):
        return self.Name
    

class newsletter(models.Model):
    BIG_TEXT = models.CharField(max_length=200,blank=True)
    MEDIUM_TEXT = models.CharField(max_length=200,blank=True)
    SMALL_TEXT = models.CharField( max_length=2000,blank=True)
    IMAGE = models.ImageField(upload_to='images/newsletter',blank=True)