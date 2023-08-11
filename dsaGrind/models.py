from django.db import models

# Create your models here.
class problem(models.Model):
    name = models.CharField(max_length=500)
    desc = models.TextField()
    difficulty = models.CharField(max_length=200)
class testcase(models.Model):
    # when a particular question is deleted it will delete all things related to that(on cascade use)
    question = models.ForeignKey(problem,on_delete=models.CASCADE)
    test = models.TextField()
    result = models.TextField()
 

