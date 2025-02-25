# Generated by Django 4.2.5 on 2025-02-25 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0010_prestamos_fecha_de_aprobacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamos',
            name='tasa_intereses',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
