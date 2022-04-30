from django.db import models
from modelapp.models import Product


# Create your models here.
class Category(models.Model):
    # url_name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='modelapp/static/image/category/')
    cat_title = models.CharField(max_length=200, null = True, blank = True)

    def __str__(self):
        return f'{self.cat_title}'


class Subcategory1(models.Model):
    sub1_title = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='cats_title')
    sub1_image = models.ImageField(upload_to='modelapp/static/image/subcategory1/')
    subcategory1_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.subcategory1_name}'


class Subcategory2(models.Model):
    product_title = models.ForeignKey(Subcategory1, on_delete=models.CASCADE, null=True, related_name='subcategory1s_name')
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
