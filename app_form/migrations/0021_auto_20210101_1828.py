# Generated by Django 2.2 on 2021-01-01 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_form', '0020_tdtskuproduct_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tdtskuproduct',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
