# Generated by Django 5.0.6 on 2024-06-08 05:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0002_alter_categoryservice_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='indicator_service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Servicios.indicator', verbose_name='Indicador de descuento'),
        ),
    ]
