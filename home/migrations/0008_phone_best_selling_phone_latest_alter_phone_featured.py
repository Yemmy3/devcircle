# Generated by Django 4.0.6 on 2022-07-21 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_phone_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='best_selling',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='latest',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='featured',
            field=models.BooleanField(),
        ),
    ]
