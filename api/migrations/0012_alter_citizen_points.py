# Generated by Django 4.2.2 on 2023-07-18 20:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_citizen_cep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizen',
            name='points',
            field=models.IntegerField(default=50, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
