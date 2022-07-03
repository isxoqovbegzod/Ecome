from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path("shop-grid/", shop_grid, name="shop_grid"),
    path("page/", page_view, name="page"),
    path("blog/", blog_view, name="blog"),
    path("contact/", contact_view, name="contact"),
    path('categoriy/<int:id>/<str:cat_title>', subcategory_1, name='subcategory_1'),
    path('categoriy/<str:cat_title>/<str:subcategory1_name>/<int:id>', subcategory_2, name='subcategory_2'),
    path('product/view/<str:product_model_name>/<int:id>', product_view, name='product_view')

]

