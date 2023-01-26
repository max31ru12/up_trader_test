from itertools import groupby

from django.db import models
from django.urls import reverse

# Create your models here.


class Menu(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название меню')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('', kwargs={'Menu_title': self.title})

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ['id']


class LevelOne(models.Model):
    title = models.CharField(max_length=64, verbose_name='Имя первого уровня')
    parent = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='Имя меню')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Level', kwargs={'level_name': self.pk})

    class Meta:
        verbose_name = 'Первый уровень вложенности'
        verbose_name_plural = 'Первые уровни вложенности'
        ordering = ['id']


class LevelTwo(models.Model):
    title = models.CharField(max_length=64, verbose_name='Имя второго уровня')
    parent = models.ForeignKey(LevelOne, on_delete=models.CASCADE, verbose_name='Родитель')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('LevelTwo', kwargs={'level_name': self.title})

    class Meta:
        verbose_name = 'Второй уровень вложенности'
        verbose_name_plural = 'Вторые уровни вложенности'
        ordering = ['id']








