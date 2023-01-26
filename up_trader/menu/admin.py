from django.contrib import admin
from .models import *

# Register your models here.


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )


class LevelOneAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent')


class LevelTwoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent')


admin.site.register(Menu, MenuAdmin)
admin.site.register(LevelOne, LevelOneAdmin)
admin.site.register(LevelTwo, LevelTwoAdmin)

