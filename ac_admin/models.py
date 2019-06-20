from django.db import models
from ac_login.models import Login


# ac_admin model

class Department(models.Model):
    name = models.CharField(max_length=50,primary_key=True)

class Officer(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    deparment = models.ForeignKey(Department,on_delete=models.CASCADE)
    contact = models.IntegerField()
    image = models.ImageField(upload_to='officer/')
    username = models.ForeignKey(Login,on_delete=models.CASCADE)

