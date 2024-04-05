from django.db import models
import datetime 

#Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 
    
class Customer(models.Model):
    first_name =  models.CharField(max_length = 50)
    last_name =  models.CharField(max_length = 50)
    phone =  models.CharField(max_length = 12)
    email  =  models.CharField(max_length = 50)
#Product Model 
class Product(models.Model):
    name = models.CharField(max_length = 100, null = False, blank = False)
    price = models.DecimalField(default = 0, decimal_places = 2, max_digits = 7)
    description =  models.CharField(max_length = 100, null = True, blank = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE) 
    image = models.ImageField(upload_to='products/', null = False, blank = False) 
    # description = models.CharField(max_length = 50, default='', blank=True, null=True)
    def __str__(self):
        return self.name