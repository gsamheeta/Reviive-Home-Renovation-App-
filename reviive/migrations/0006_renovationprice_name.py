# Generated by Django 4.2.6 on 2023-11-16 03:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reviive', '0005_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='renovationprice',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]