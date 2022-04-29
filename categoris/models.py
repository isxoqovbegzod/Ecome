from django.db import models
from modelapp.models import Product


# Create your models here.
class Category(models.Model):
    # url_name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='modelapp/static/image/category/')
    cat_title = models.SlugField(max_length=200, null = True, blank = True)

    def __str__(self):
        return f'{self.cat_title}'


class Subcategory1(models.Model):
    sub1_title = models.ForeignKey(Category, on_delete=Category, null=True, related_name='cats_title')
    sub1_image = models.ImageField(upload_to='modelapp/static/image/subcategory1/')
    subcategory1_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.subcategory1_name}'


# class Subcategory2(models.Model):
#     category_title = models.ForeignKey(Subcategory1, on_delete=models.CASCADE, related_name='subcategorys1_name')
#     image = models.ImageField(upload_to='image/subcategory2/')
#     category_price = models.FloatField()
#     category_credit_price = models.FloatField()
#     category_model_name = models.CharField(max_length=200)
