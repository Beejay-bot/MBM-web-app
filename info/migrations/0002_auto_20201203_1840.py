# Generated by Django 3.1.3 on 2020-12-03 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name_plural': 'About Us'},
        ),
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name_plural': 'Contact Us'},
        ),
    ]
