from django.db import models

# Create your models here.
class introduction(models.Model):
    BIG_TEXT = models.CharField(max_length=200)
    MEDIUM_TEXT = models.CharField(max_length=200)
    SMALL_TEXT = models.CharField(max_length=200)
    Profile_image = models.ImageField(upload_to='images',default='facweb - Copy\textutils\static\public\playground_assets\puneet gupta-1500w.png')
    LINK_1 = models.CharField(max_length=200)
    LINK_1_URL = models.CharField(max_length=200,choices=[("index","Home Page"),("mywork","My Work Section"),("aboutme","About Me Section"),("contact","Contact Me Section"),("research","Research Group Section"),("students","Students Portal Section"),("discussion","Discussion Section")])
    LINK_2 = models.CharField(max_length=200)
    LINK_2_URL = models.CharField(max_length=200,choices=[("index","Home Page"),("mywork","My Work Section"),("aboutme","About Me Section"),("contact","Contact Me Section"),("research","Research Group Section"),("students","Students Portal Section"),("discussion","Discussion Section")])

class testimonials(models.Model):
    Description = models.CharField('testimonial description',max_length=500)
    Name = models.CharField('testimonial name',max_length=200)
    Designation = models.CharField('testimonial designation',max_length=200)
    Photo = models.ImageField('testimonial photo',upload_to='images',default='settings.MEDIA_ROOT/default.png')

    def __str__(self):
        return self.Name