# Generated by Django 2.2 on 2020-12-12 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_form', '0018_auto_20201212_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tdtskuproduct',
            name='id_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_form.TdtProduct'),
        ),
    ]
