# Generated by Django 2.2 on 2020-12-08 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_form', '0010_auto_20201208_1846'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cdtproductcolor',
            options={'verbose_name': 'Product Color', 'verbose_name_plural': 'Products Colors'},
        ),
        migrations.RemoveField(
            model_name='cdtproductcolor',
            name='id_photo',
        ),
        migrations.AddField(
            model_name='cdtproductphoto',
            name='id_product_color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_form.CdtProductColor'),
        ),
    ]