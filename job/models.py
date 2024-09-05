from typing import Iterable
from django.db import models
from django.utils.text import slugify

from django.contrib.auth.models import User
'''
django models fields
    - html widget
    - validation
    - db size
'''
def image_upload(instance,filename):
    imgaename, extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id, extension)

JOB_TYPE = {
    ("Full Time","Full Time"),
    ("Part Time","Part Time")
}
# Create your models here.
class Job(models.Model):
    onwer = models.ForeignKey(User, related_name='onwer', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    # location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField()
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete= models.CASCADE, blank= True) 
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True, null=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args,**kwargs)

    def __str__(self):
        return self.title
    


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    
class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name