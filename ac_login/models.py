from django.db import models

# ac_login

class Login(models.Model):
    username = models.CharField(primary_key=True,max_length=30)
    password = models.CharField(max_length=30)
    usertype = models.CharField(max_length=10)
