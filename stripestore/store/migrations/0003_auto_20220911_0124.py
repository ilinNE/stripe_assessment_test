# Generated by Django 3.2.15 on 2022-09-11 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_auto_20220911_0113"),
    ]

    operations = [
        migrations.AddField(
            model_name="discount",
            name="coupon_id",
            field=models.CharField(
                default="asdasd",
                max_length=32,
                verbose_name="Stripe Coupon ID",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="discount",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="store.discount",
                verbose_name="Скидка",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="tax",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="store.tax",
                verbose_name="Налог",
            ),
        ),
    ]
