# Generated by Django 4.2.6 on 2023-11-16 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviive', '0014_renovationprice_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='renovationprice',
            name='user',
        ),
    ]
