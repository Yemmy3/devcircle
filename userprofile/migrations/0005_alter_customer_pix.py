# Generated by Django 4.0.6 on 2022-08-16 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_alter_customer_pix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='pix',
            field=models.ImageField(upload_to='customer'),
        ),
    ]
