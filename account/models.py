from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.CharField(max_length=40, null=False, unique=True)
    pwd = models.CharField(max_length=400, null=False)
    name = models.CharField(max_length=40, null=False, unique=True)
    birth = models.DateField(null=False)
    gender = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=300, null=False, unique=True)

    def __str__(self):
        return self.uid
