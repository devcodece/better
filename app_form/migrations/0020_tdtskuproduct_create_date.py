# Generated by Django 2.2 on 2020-12-21 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_form', '0019_auto_20201212_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='tdtskuproduct',
            name='create_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
