from django.db import models


'''
django models fields
    - html widget
    - validation
    - db size
'''

JOB_TYPE = {
    ("Full Time","Full Time"),
    ("Part Time","Part Time")
}
# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    # location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField()
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete= models.CASCADE, blank= True) 

    def __str__(self):
        return self.title
    


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    