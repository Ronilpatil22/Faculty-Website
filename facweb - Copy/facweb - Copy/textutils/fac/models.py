from django.db import models

# Create your models here.
class testimonials(models.Model):
    Description = models.CharField('testimonial description',max_length=50)
    Name = models.CharField('testimonial name',max_length=120)
    Designation = models.CharField('testimonial designation',max_length=120)
    Photo = models.ImageField('testimonial photo',upload_to='images')

    def __str__(self):
        return self.Name