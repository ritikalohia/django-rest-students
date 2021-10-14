from django.db import models

# Create your models here.
class Student(models.Model):
    # st_name = models.CharField(max_length=200)
    # age = models.IntegerField()
    # roll_num = models.IntegerField()
    # standard = models.CharField(max_length=200)
    body = models.CharField(max_length=200)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.st_name

    class Meta:
        ordering = ['-updated']