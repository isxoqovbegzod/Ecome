from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register([Category, Subcategory1, Subcategory2])
admin.site.register(AllData)
admin.site.register(NewDate)

