# Generated by Django 4.2.6 on 2023-11-15 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_details_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='role',
            field=models.CharField(default='regular', max_length=50),
        ),
    ]