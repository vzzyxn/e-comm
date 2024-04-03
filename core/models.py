from django.db import models
import datetime 

#Category Model
class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name 
    

#Product Model 
class Product(models.Model):
    name = models.CharField(max_length = 100, null = False, blank = False)
    price = models.DecimalField(default = 0, decimal_places = 2, max_digits = 7)
    details =  models.CharField(max_length = 100, null = True, blank = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE) 
    image = models.ImageField(upload_to='products/', null = False, blank = False) 

    def __str__(self):
        return self.name