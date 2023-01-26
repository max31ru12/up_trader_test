from django.urls import path, re_path, include
from .views import *


urlpatterns = [
    path('', get_menu, name='menu'),
    path('<str:lvl_1>/', show_level_one, name='level_one'),
    path('<str:lvl_1>/<str:lvl_2>/', show_level_two, name='level_two'),
    path('<str:lvl_1>/<str:lvl_2>/<str:lvl_3>/', get_product, name='product_page')
]

