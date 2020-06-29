from django.db import models

# Create your models here.
class Products:
    name : str
    img : str
    desc : str
    price : float

class selling(models.Model):
    price = models.FloatField(max_length = 10)
    product_name = models.CharField(max_length = 50)
    product_image = models.CharField(max_length = 100, null = True)
