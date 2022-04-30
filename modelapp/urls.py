from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('categoriy/<int:id>/<str:cat_title>', subcategory_1, name='subcategory_1'),
    path('categoriy/<str:cat_title>/<str:subcategory1_name>/<int:id>', subcategory_2, name='subcategory_2'),
    path('product/view/<str:product_model_name>/<int:id>', product_view, name='product_view')

]

