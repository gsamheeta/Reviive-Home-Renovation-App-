# Generated by Django 4.2.6 on 2023-11-16 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviive', '0008_remove_renovationprice_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renovationprice',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]