# Generated by Django 4.2.2 on 2023-07-18 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_citizen_cep_alter_city_cep_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citizen',
            name='cep',
        ),
    ]