from django.db import models

# Create your models here.
class current_research(models.Model):
    Image = models.ImageField(upload_to='current_research/images',blank=True)
    Name = models.CharField(max_length=2000)
    Period = models.CharField(max_length=2000,blank=True)
    Area_of_research = models.CharField(max_length=2000,blank=True)
    discipline = models.CharField(max_length=2000,blank=True)
    google_scholar_link = models.URLField()
    linkedin_link = models.URLField()
    mail = models.EmailField()


    def __str__(self):
        return self.Name
    

class alumni_phd(models.Model):
    Image = models.ImageField(upload_to='current_research/images',blank=True)
    Name = models.CharField(max_length=2000)
    Period = models.CharField(max_length=2000,blank=True)
    Area_of_research = models.CharField(max_length=2000,blank=True)
    google_scholar_link = models.URLField()
    linkedin_link = models.URLField()
    mail = models.EmailField()

    def __str__(self):
        return self.Name
    

class alumni_ms(models.Model):
    Image = models.ImageField(upload_to='current_research/images',blank=True)
    Name = models.CharField(max_length=2000)
    Period = models.CharField(max_length=2000,blank=True)
    Area_of_research = models.CharField(max_length=2000,blank=True)
    google_scholar_link = models.URLField()
    linkedin_link = models.URLField()
    mail = models.EmailField()

    def __str__(self):
        return self.Name
    

class alumni_btech(models.Model):
    Image = models.ImageField(upload_to='current_research/images',blank=True)
    Name = models.CharField(max_length=2000)
    Period = models.CharField(max_length=2000,blank=True)
    Position = models.CharField(max_length=2000,blank=True)
    Company = models.CharField(max_length=2000,blank=True)

    def __str__(self):
        return self.Name
    

class interns(models.Model):
    Image = models.ImageField(upload_to='current_research/images',blank=True)
    Name = models.CharField(max_length=2000)
    Period = models.CharField(max_length=2000,blank=True)
    Education = models.CharField(max_length=2000,blank=True)
    Area_of_research = models.CharField(max_length=2000,blank=True)

    def __str__(self):
        return self.Name
    

class current_btp(models.Model):
    Image = models.ImageField(upload_to='current_research/images',blank=True)
    Name = models.CharField(max_length=2000)
    Period = models.CharField(max_length=2000,blank=True)

    def __str__(self):
        return self.Name