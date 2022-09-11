# Generated by Django 3.2.15 on 2022-09-11 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Discount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=128, verbose_name="Название"),
                ),
                ("descpiption", models.TextField(verbose_name="Описание")),
                ("price", models.PositiveIntegerField(verbose_name="Цена")),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
            },
        ),
        migrations.CreateModel(
            name="ItemInOrder",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "quantity",
                    models.PositiveIntegerField(verbose_name="Количество"),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store.item",
                        verbose_name="Товар",
                    ),
                ),
            ],
            options={
                "verbose_name": "Заказанный товар",
                "verbose_name_plural": "Заказанные товары",
            },
        ),
        migrations.CreateModel(
            name="Tax",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=128, verbose_name="Название"),
                ),
                (
                    "inclusive",
                    models.BooleanField(
                        default=False, verbose_name="Включен в цену"
                    ),
                ),
                (
                    "percentage",
                    models.FloatField(verbose_name="Налоговая ставка"),
                ),
                (
                    "country",
                    models.CharField(max_length=2, verbose_name="Код страны"),
                ),
                ("stripe_id", models.CharField(blank=True, max_length=32)),
            ],
            options={
                "verbose_name": "Налог",
                "verbose_name_plural": "Налоги",
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "items",
                    models.ManyToManyField(
                        related_name="items",
                        through="store.ItemInOrder",
                        to="store.Item",
                        verbose_name="Товары",
                    ),
                ),
            ],
            options={
                "verbose_name": "Заказ",
                "verbose_name_plural": "Заказы",
            },
        ),
        migrations.AddField(
            model_name="iteminorder",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="store.order",
                verbose_name="Заказ",
            ),
        ),
    ]