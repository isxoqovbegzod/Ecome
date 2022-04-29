from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('categoriy/<str:cat_title>', subcategory_1, name='subcategory_1'),

]

