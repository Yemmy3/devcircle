# Generated by Django 4.0.6 on 2022-07-19 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(default='a', unique=True),
        ),
    ]
