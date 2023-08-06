# Generated by Django 3.2 on 2023-08-04 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_piezasrepuesto_imagen_tienda'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProformaManoDeObra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True)),
                ('validez', models.CharField(max_length=20)),
                ('correo', models.CharField(blank=True, max_length=200)),
                ('celular', models.CharField(blank=True, max_length=9)),
                ('actividad', models.CharField(blank=True, max_length=500)),
                ('observacion', models.CharField(blank=True, max_length=500)),
                ('bu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.bu')),
                ('condicion_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.pago')),
                ('moneda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.moneda')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='ProformaConsultoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True)),
                ('validez', models.CharField(max_length=20)),
                ('correo', models.CharField(blank=True, max_length=200)),
                ('celular', models.CharField(blank=True, max_length=9)),
                ('actividad', models.CharField(blank=True, max_length=500)),
                ('observacion', models.CharField(blank=True, max_length=500)),
                ('bu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.bu')),
                ('condicion_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.pago')),
                ('moneda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.moneda')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.vendedor')),
            ],
        ),
    ]