# Generated by Django 4.2.8 on 2024-03-20 23:16

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_book_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=33.33, max_digits=1000, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))]),
        ),
    ]