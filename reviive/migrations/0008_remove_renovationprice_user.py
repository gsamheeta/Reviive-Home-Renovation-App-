# Generated by Django 4.2.6 on 2023-11-16 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviive', '0007_renovationprice_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='renovationprice',
            name='user',
        ),
    ]
