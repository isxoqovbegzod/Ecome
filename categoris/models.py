from django.db import models
from modelapp.models import Product


# Create your models here.
class Category(models.Model):
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
    COLOR_PROD = [
        ("White", "White"),
        ("Red", "Red"),
        ("Blue", "Blue"),
        ("Gray", "Gray"),
        ("Black", "Black"),
        ("Green", "Green"),
    ]

    product_title = models.ForeignKey(Subcategory1, on_delete=models.CASCADE, null=True, related_name='subcategory1s_name')
    product_model_name = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to='modelapp/static/image/product/')
    product_price = models.CharField(max_length=200)
    product_old_price = models.CharField(max_length=200)
    product_color = models.CharField(max_length=5, choices=COLOR_PROD, null=True, blank=True)
    product_credit_price = models.FloatField()
    short_description = models.TextField()

    deep_description = models.TextField()
    characteristics = models.JSONField(default=dict)
    comment = models.JSONField(default=dict)

    def __str__(self):
        return f'{self.product_model_name}'


class AllData(models.Model):
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    insta_link = models.CharField(max_length=255)
    telegram_link = models.CharField(max_length=255)
    facebock_link = models.CharField(max_length=255)


class NewDate(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    new_image = models.ImageField(upload_to='modelapp/static/image/new/')
    crete_date = models.DateTimeField(auto_now=True)








