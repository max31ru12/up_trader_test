from django import template
from menu.models import *

# регистрация собственных тэгов
register = template.Library()


@register.simple_tag()
def get_menu():
    return Menu.objects.all()


@register.simple_tag()
def get_lvl_one():
    return LevelOne.objects.all()


@register.simple_tag()
def get_lvl_two():
    return LevelTwo.objects.all()

