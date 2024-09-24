from django.db import models
# Create your models here.

class Blogs(models.Model):
    title=models.CharField(max_length=200,blank=False,)
    subtitle=models.CharField(max_length=100,blank=False,null=False)
    description=models.TextField()
    image=models.ImageField(upload_to="images",blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

