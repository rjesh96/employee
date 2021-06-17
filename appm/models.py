from django.db import models


class Employee(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    doj = models.DateField(auto_now_add=True)
    designation=models.CharField(max_length=30)

