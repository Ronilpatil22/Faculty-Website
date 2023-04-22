from django.db import models

# Create your models here.
class current_employment(models.Model):
    Text = models.CharField(max_length=200000)

class previous_employment(models.Model):
    Text = models.CharField(max_length=200000)

class projects(models.Model):
    Title = models.CharField(max_length=200000,blank=True)
    Project_investigator = models.CharField(max_length=200000,blank=True)
    Sponsoring = models.CharField(max_length=20000,blank=True)
    Duration = models.CharField(max_length=20000,blank=True)
    Status = models.CharField(max_length=200000,blank=True)

class awards(models.Model):
    Name = models.CharField(max_length=200000,blank=True)
    Awarding_agency = models.CharField(max_length=200000,blank=True)
    Year = models.CharField(max_length=200000,blank=True)
    
class international_journal(models.Model):
    Text = models.CharField(max_length=200000)

class conference_papers(models.Model):
    Text = models.CharField(max_length=200000)

class patents(models.Model):
    Text = models.CharField(max_length=200000)

class book_chapters(models.Model):
    Text = models.CharField(max_length=200000)

class achievements_outreach(models.Model):
    Text = models.CharField(max_length=200000)

class courses(models.Model):
    Text = models.CharField(max_length=200000)
