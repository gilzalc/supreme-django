# Generated by Django 4.2.8 on 2024-03-20 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0004_alter_author_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birth_date',
            field=models.DateField(default=None, null=True),
        ),
    ]
