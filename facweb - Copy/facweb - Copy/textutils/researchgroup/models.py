from django.db import models

# Create your models here.
class research_group_class(models.Model):
    Name_of_class = models.CharField(max_length=2000,blank=True)

    def __str__(self):
        return self.Name_of_class

class research_group_details(models.Model):
    Class = models.ForeignKey("research_group_class", verbose_name=("Name_of_class"), on_delete=models.CASCADE)
    Name = models.CharField(max_length=2000,blank=True)
    Image = models.ImageField(upload_to='images/researchgroup',blank=True)

    def __str__(self):
        return self.Name