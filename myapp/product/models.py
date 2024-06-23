from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    text= models.CharField(max_length=250)
    date= models.DateTimeField(auto_now_add=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    
