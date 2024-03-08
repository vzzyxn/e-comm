from django.db import models
import datetime 

# Category model
class Category(models.Model):
    name = models.CharField(max_length = 60)

    def __str__(self):
        return self.name
    
# Customer model  
class Customer(models.Model):
    first_name = models.CharField(max_length = 30) 
    last_name = models.CharField(max_length = 30)
    password = models.CharField(max_length = 100) 
    email = models.EmailField(max_length = 60)
    phone = models.CharField(max_length = 13) 

    def __str__(self):  
        return self.first_name, self.last_name, self.password, self.email, self.phone

# Product model 
class Product(models.Model):
    name = models.CharField(max_length = 60) 
    price = models.DecimalField(default = 0, decimal_places = 2, max_digits = 7)
    category = models.ForeignKey(Category, on_delete = models.CASCADE) 
    description =  models.CharField(max_length = 200, default = '', blank = True, null = True)
    image = models.ImageField(upload_to = 'products/', blank = True, null = True)
    def __str__ (self):
        return self.name

# Order model 
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 1)
    phone = models.CharField(max_length = 13)
    address = models.CharField(max_length = 100, blank = True, null = True)
    date = models.DateField(datetime.datetime.today)
    status = models.BooleanField(default = False) 

    def __str__(self): 
        return  self.product