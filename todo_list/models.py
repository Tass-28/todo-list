from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.TextField()
    is_complete=models.BooleanField()
    due_date=models.DateField()
    

