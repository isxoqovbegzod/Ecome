from django.shortcuts import render
from categoris.models import *


# Create your views here.

def home(request):
    new_data = NewDate.objects.all()
    feategorys = Subcategory2.objects.all()
    category = Category.objects.all()
    top_phones = feategorys.filter(product_title=7)
    top_cars = feategorys.filter(product_title=11)
    top_sports = feategorys.filter(product_title=10)
    context = {
        "categorys": category,
        "featured_category": feategorys,
        "top_phones": top_phones,
        "top_cars": top_cars,
        "top_sports": top_sports,
        "new_datas": new_data
    }
    return render(request, 'index.html', context)


def shop_grid(request):
    all_category = Category.objects.all()
    category = Subcategory2.objects.all()

    li = []
    for i in category:
        li.append(i.product_price)
    context = {
        "categorys": category,
        "all_category": all_category
    }
    return render(request, "shop-grid.html", context)


def page_view(request):
    all_category = Category.objects.all()

    context = {
        "all_category": all_category
    }
    return render(request, "page_view.html", context)


def blog_view(request):
    all_category = Category.objects.all()
    new_date = NewDate.objects.all()
    context = {
        "all_category": all_category,
        "new_dates": new_date,
    }
    return render(request, "blog.html", context)


def contact_view(request):
    all_category = Category.objects.all()
    data_date = AllData.objects.all()
    phone = []
    email = []
    telegram_link = []
    insta_link = []
    address = []
    description = []

    for date_new in data_date:
        phone = date_new.phone
        email = date_new.email
        telegram_link = date_new.telegram_link
        insta_link = date_new.insta_link
        address = date_new.address
        description =date_new.description

    context = {
        "all_category": all_category,
        "email": email,
        "telegram_link": telegram_link,
        "insta_link": insta_link,
        "address": address,
        "description": description,
        "phone": phone
    }
    return render(request, "conact.html", context)


def subcategory_1(request, id, cat_title):
    category = Subcategory1.objects.all()
    res = category.filter(sub1_title=id)
    context = {"categorys": res}

    return render(request, 'categiry.html', context)


def subcategory_2(request, cat_title, subcategory1_name, id):
    all_category = Category.objects.all()
    category = Subcategory2.objects.all()
    res = category.filter(product_title=id)
    li = []
    for i in res:
        li.append(i.product_price)
    context = {
        "categorys": res,
        "all_category": all_category
    }

    return render(request, 'sub1category.html', context)


def product_view(request, product_model_name, id):
    category = Subcategory2.objects.filter(id=id)
    res = category.get().characteristics
    all_category = Category.objects.all()
    context = {
        "categorys": category,
        'characteristics': res,
        "all_category": all_category
    }
    return render(request, 'product_view.html', context)
