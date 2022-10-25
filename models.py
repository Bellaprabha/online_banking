from django.db import models
# from matplotlib.pyplot import title
#from datetime import datetime

# Create your models here.

class Customers(models.Model):
    customerid=models.BigIntegerField()
    name=models.CharField(max_length=20)
    Account_no=models.BigIntegerField()
    Branch=models.CharField(max_length=20)
    IFSC=models.CharField(max_length=10)
    phone=models.BigIntegerField()
    Address=models.CharField(max_length=100)


      



    
