# Generated by Django 4.0.4 on 2022-05-28 17:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipohabitacion',
            old_name='caracteristicas',
            new_name='descripcion',
        ),
        migrations.AlterField(
            model_name='checkout',
            name='fecha_salida',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 28, 17, 18, 33, 762087, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha_factura',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 28, 17, 18, 33, 765087, tzinfo=utc)),
        ),
    ]
