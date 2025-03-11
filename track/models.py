from django.db import models


class Track(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    location =  models.CharField(max_length=50)
    createdate=models.DateTimeField(auto_now_add=True)
    updatedate=models.DateTimeField(auto_now=True)
    isactive=models.BooleanField(default=True)
    def __str__(self):
        return self.name

