from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    descpiption = models.TextField(verbose_name="Описание")
    price = models.PositiveIntegerField(verbose_name="Цена")
    
    class Meta:
        verbose_name = "Вещь"
        verbose_name_plural = "Вещи"
    