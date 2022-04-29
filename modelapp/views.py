from django.shortcuts import render
from categoris.models import *


# Create your views here.

def home(request):
    category = Category.objects.all()
    context = {"categorys": category}
    return render(request, 'index.html', context)


def subcategory_1(request, cat_title):
    category = Subcategory1.objects.get()
    context = {"categorys": category}
    return render(request, 'sub2.html', context)











