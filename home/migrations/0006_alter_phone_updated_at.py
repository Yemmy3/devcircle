# Generated by Django 4.0.6 on 2022-07-19 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_phone_updated_at_alter_phone_uploaded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
