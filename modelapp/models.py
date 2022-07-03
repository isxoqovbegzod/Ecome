from django.db import models


# Create your models here.

class Product(models.Model):
    product_model_name = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to='modelapp/static/image/product/')
    product_price = models.FloatField()
    product_credit_price = models.FloatField()
    short_description = models.TextField()

    deep_description = models.TextField()
    characteristics = models.JSONField(default=dict)
    comment = models.JSONField(default=dict)

    def __str__(self):
        return f'{self.product_model_name}'



