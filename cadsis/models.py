from django.db import models

# Create your models here.
class Products(models.Model):
    product_name    = models.CharField(max_length=30)
    product_codebar = models.CharField(max_length=30)