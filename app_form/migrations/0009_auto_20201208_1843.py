# Generated by Django 2.2 on 2020-12-08 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_form', '0008_auto_20201208_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cdtproductphoto',
            name='id_product_color',
        ),
        migrations.AddField(
            model_name='cdtproductcolor',
            name='id_photo',
            field=models.ManyToManyField(to='app_form.CdtProductPhoto'),
        ),
    ]