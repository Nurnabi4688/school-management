from django.db import models

from. constant import DEPARTMENT,GENDER

class Register(models.Model):
    name=models.CharField(max_length=30)
    father_name=models.CharField(max_length=30)
    mother_name=models.CharField(max_length=30)
    gender=models.CharField(choices=GENDER)
    phone_no=models.CharField(max_length=11)
    email=models.EmailField()
    department=models.CharField(choices=DEPARTMENT)

    def __str__(self):
        return self.name
    
