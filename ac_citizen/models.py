from django.db import models
from ac_login.models import Login
from ac_admin.models import Department

# ac_citizen

class CitizenRegister(models.Model):
    ctid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    contact = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=20)
    image = models.ImageField(upload_to='citizen/')
    username = models.ForeignKey(Login,on_delete=models.CASCADE)
    status = models.CharField(max_length=30,default=False)


class Complaint(models.Model):
    cid = models.IntegerField(primary_key=True)
    ctid = models.ForeignKey(CitizenRegister,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,default=False)
    message = models.TextField()
    image = models.ImageField(upload_to='complaints/')
    registerdate = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10)
    closedate = models.DateField(default=None,null=True)

class Feeback(models.Model):
    fid = models.IntegerField(primary_key=True)
    cid = models.ForeignKey(Complaint,on_delete=models.CASCADE)
    ctid = models.ForeignKey(CitizenRegister,on_delete=models.CASCADE)
    message = models.TextField()
    image = models.ImageField(upload_to='feedback/')

class OTP(models.Model):
    contact = models.IntegerField(primary_key=True)
    otp = models.CharField(max_length=30)