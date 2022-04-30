from django.shortcuts import render
from categoris.models import *


# Create your views here.

def home(request):
    category = Category.objects.all()
    context = {"categorys": category}
    return render(request, 'index.html', context)


def subcategory_1(request, id, cat_title):
    category = Subcategory1.objects.all()
    res = category.filter(sub1_title=id)
    context = {"categorys": res}

    return render(request, 'categiry.html', context)


def subcategory_2(request, cat_title, subcategory1_name, id):
    category = Subcategory2.objects.all()
    res = category.filter(product_title=id)
    context = {"categorys": res}
    return render(request, 'sub1category.html', context)


def product_view(request, product_model_name, id):
    category = Subcategory2.objects.filter(id=id)
    context = {"categorys":category}
    return render(request, 'product_view.html', context)







