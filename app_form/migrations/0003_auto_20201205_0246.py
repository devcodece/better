# Generated by Django 2.2 on 2020-12-05 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_form', '0002_auto_20201204_1536'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cdtcolor',
            options={'verbose_name': 'Color', 'verbose_name_plural': 'Colors'},
        ),
        migrations.AlterModelOptions(
            name='cdtproductphoto',
            options={'verbose_name': 'Photo', 'verbose_name_plural': 'Photos'},
        ),
    ]