# Generated by Django 4.2.5 on 2025-02-23 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0007_alter_clientes_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='identificacion',
            field=models.CharField(default='123456789', max_length=45, unique=True),
        ),
    ]
