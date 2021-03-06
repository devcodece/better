# Generated by Django 2.2 on 2020-12-08 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_form', '0011_auto_20201208_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='tdtskuproduct',
            name='id_product_color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app_form.CdtProductColor'),
        ),
        migrations.AlterField(
            model_name='tdtskuproduct',
            name='id_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app_form.TdtProduct'),
        ),
        migrations.AlterField(
            model_name='tdtskuproduct',
            name='id_size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app_form.CdtSize'),
        ),
    ]
