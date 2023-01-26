from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import *
# Create your views here.


def get_menu(request):
    return render(request, 'menu/start_page.html')


def show_level_one(request, lvl_1):
    context = {'selected_menu': lvl_1}
    return render(request, 'menu/level_one_page.html', context=context)


def show_level_two(request, lvl_1, lvl_2):
    context = {'selected_menu': lvl_1,
               'selected_one': lvl_2}
    return render(request, 'menu/level_two_page.html', context=context)


def get_product(request, lvl_1, lvl_2, lvl_3):
    return HttpResponse(f'Отображение продукта с именем {lvl_3}')



