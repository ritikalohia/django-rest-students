from django.db import models

# Create your models here.
class student(models.Models):
    st_name = models.CharField(max_length=200)
    age = models.IntegerField()
    roll_num = models.IntegerField()
    start = models.CharField(max_length=200)