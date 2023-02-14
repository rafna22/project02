from django.db import models

# Create your models here.
class usertab(models.Model):
 username=models.CharField(max_length=100)
 password=models.CharField(max_length=100)
 email=models.CharField(max_length=200)
 image=models.ImageField(upload_to='media/')

class cont_tb(models.Model):
 name=models.CharField(max_length=100)
 email=models.CharField(max_length=200)
 message=models.CharField(max_length=300)