from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    descpiption = models.TextField(verbose_name="Описание")
    price = models.PositiveIntegerField(verbose_name="Цена")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class Discount(models.Model):
    class Duration(models.TextChoices):
        FOREVER = "forever", "Постоянный"
        ONCE = "once", "Одноразовый"
        REPEATING = "repeating", "Временный"

    name = models.CharField(max_length=128, verbose_name="Название")
    coupon_id = models.CharField(
        max_length=32, verbose_name="Stripe Coupon ID"
    )
    amount_off = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Размер фиксированной скидки"
    )
    duration = models.CharField(
        max_length=16,
        choices=Duration.choices,
        verbose_name="Длительность действия",
    )
    percent_off = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
        verbose_name="Размер скидки в процентах",
        blank=True,
        null=True,
    )
    duration_in_months = models.PositiveIntegerField(
        verbose_name="Длительность действия временной скидки",
        blank=True,
        null=True,
    )
    max_redemptions = models.PositiveIntegerField(
        verbose_name="Количество применений", blank=True, null=True
    )

    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"

    def __str__(self):
        return self.name


class Tax(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    inclusive = models.BooleanField(
        default=False, verbose_name="Включен в цену"
    )
    percentage = models.FloatField(
        verbose_name="Налоговая ставка",
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
    )
    country = models.CharField(max_length=2, verbose_name="Код страны")
    description = models.TextField(verbose_name="Описание")
    stripe_id = models.CharField(
        max_length=32, verbose_name="Stripe TaxRate ID"
    )

    class Meta:
        verbose_name = "Налог"
        verbose_name_plural = "Налоги"

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(
        Item,
        through="ItemInOrder",
        verbose_name="Товары",
    )
    tax = models.ForeignKey(
        Tax,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Налог",
    )
    discount = models.ForeignKey(
        Discount,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Скидка",
    )

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f" Заказ №{self.id}"


class ItemInOrder(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        verbose_name="Товар",
    )
    quantity = models.PositiveIntegerField(
        verbose_name="Количество", validators=[MinValueValidator(1)], default=1
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name="Заказ",
    )

    class Meta:
        verbose_name = "Заказанный товар"
        verbose_name_plural = "Заказанные товары"

    def __str__(self):
        return f"{self.item.name} / Заказ №{self.order.id}"
