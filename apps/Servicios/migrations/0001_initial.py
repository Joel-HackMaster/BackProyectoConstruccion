# Generated by Django 5.0.6 on 2024-06-07 18:39

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryService',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('description', models.CharField(max_length=50, unique=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Categoria de Servicio',
                'verbose_name_plural': 'Categorias de servicio',
            },
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('descount_value', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Indicador de ofertas',
                'verbose_name_plural': 'Indicadores de oferta',
            },
        ),
        migrations.CreateModel(
            name='HistoricalCategoryService',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificacion')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de eliminacion')),
                ('description', models.CharField(db_index=True, max_length=50, verbose_name='Descripcion')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Categoria de Servicio',
                'verbose_name_plural': 'historical Categorias de servicio',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalIndicator',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificacion')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de eliminacion')),
                ('descount_value', models.PositiveSmallIntegerField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Indicador de ofertas',
                'verbose_name_plural': 'historical Indicadores de oferta',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalService',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificacion')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de eliminacion')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Nombre de servicio')),
                ('description', models.TextField(verbose_name='Descripcion del servicio')),
                ('image', models.CharField(default='', max_length=300, verbose_name='Imagen de servicio')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('category_service', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Servicios.categoryservice', verbose_name='Categoria de servicio')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('indicator_service', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Servicios.indicator', verbose_name='Indicador de descuento')),
            ],
            options={
                'verbose_name': 'historical Servicio',
                'verbose_name_plural': 'historical Servicios',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre de servicio')),
                ('description', models.TextField(verbose_name='Descripcion del servicio')),
                ('image', models.CharField(default='', max_length=300, verbose_name='Imagen de servicio')),
                ('category_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servicios.categoryservice', verbose_name='Categoria de servicio')),
                ('indicator_service', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Servicios.indicator', verbose_name='Indicador de descuento')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
    ]
