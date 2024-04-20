from django.db import models

# Create your models here.
class Task(models.Model):
    tasktitle= models.CharField(max_length=30)
    taskdesc= models.TextField()
    
    completed = models.BooleanField(default=False) 
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tasktitle