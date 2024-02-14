# Generated by Django 4.2.8 on 2024-02-14 10:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("currencies", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="currency",
            name="rate",
            field=models.DecimalField(
                blank=True,
                decimal_places=4,
                max_digits=10,
                null=True,
                verbose_name="Курс",
            ),
        ),
    ]
