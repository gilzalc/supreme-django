# Generated by Django 4.2.8 on 2024-03-12 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searchable_text', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
