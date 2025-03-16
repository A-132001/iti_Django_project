from django.db import models
from track.models import Track
class Trainee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    image = models.ImageField(upload_to='trainee/images/')
    createdate=models.DateTimeField(auto_now_add=True)
    updatedate=models.DateTimeField(auto_now=True)
    isactive=models.BooleanField(default=True)
    track=models.ForeignKey(to=Track,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    