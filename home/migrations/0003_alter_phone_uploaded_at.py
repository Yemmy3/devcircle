# Generated by Django 4.0.6 on 2022-07-19 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_phone_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='uploaded_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]