from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False, null=False)
    # link = models.URLField(max_length=200, unique=True, blank=False, null=False)
    link = models.CharField(max_length=200, unique=True, blank=False, null=False)
    image = models.ImageField(null=False, blank=False, upload_to='Portfolio/logos/')


class Project(models.Model):
    projectName = models.CharField(max_length=200, unique=True, blank=False, null=False)
    link = models.CharField(max_length=200, unique=True, blank=False, null=False)
    image = models.ImageField(null=False, blank=False, upload_to='Portfolio/projects/')
    description = HTMLField()
    technologies = models.CharField(max_length=400, blank=False, null=False)


class Home(models.Model):
    pageContent = HTMLField()





class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    blogTitle = models.CharField(max_length=400, blank=False, null=False)
    image = models.ImageField(upload_to="Portfolio/blogs/", blank=True, null=True)
    content = HTMLField()
    datePublished = models.DateTimeField(auto_now_add=True)
    
    slug = models.SlugField(max_length=400, unique=True, blank=True, null=True)
    totalViews = models.PositiveIntegerField(default=0)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.blogTitle)
        super().save(*args, **kwargs)


    def calculate_reading_time(self):   
        words_per_minute = 200
        word_count = len(self.content.split())
        reading_time_min = max(1, round(word_count / words_per_minute))
        return reading_time_min





class BaseExperience(models.Model):
    startDate = models.DateField(null=True, blank=True)
    endDate = models.DateField(null=True, blank=True)
    description = HTMLField(null=True, blank=True)
    class Meta:
        abstract = True

class WorkExperience(BaseExperience):
    companyName = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    technologies = models.CharField(max_length=200)
    is_current = models.BooleanField(default=False)
    
    def __str__(self):
        return self.companyName

class Education(BaseExperience):
    institutionName = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.institutionName
    
class Certification(BaseExperience):
    certificateName = models.CharField(max_length=200)
    institute = models.CharField(max_length=100)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.certificateName