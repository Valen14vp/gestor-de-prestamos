# Generated by Django 4.2.5 on 2024-12-17 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0003_alter_clientes_options_alter_prestamos_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestamos',
            name='tenant_id',
        ),
        migrations.RemoveField(
            model_name='recibos_prestamos',
            name='tenant_id',
        ),
        migrations.AddField(
            model_name='clientes',
            name='usuarios',
            field=models.ForeignKey(db_column='usuarios_id', default=1, on_delete=django.db.models.deletion.CASCADE, to='prestamos.usuarios'),
        ),
        migrations.AddField(
            model_name='prestamos',
            name='clientes',
            field=models.ForeignKey(db_column='clientes_id', default=1, on_delete=django.db.models.deletion.CASCADE, to='prestamos.clientes'),
        ),
        migrations.AlterField(
            model_name='recibos_prestamos',
            name='prestamos',
            field=models.ForeignKey(db_column='prestamos_id', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recibos', to='prestamos.prestamos'),
        ),
    ]
