# Generated by Django 3.2.6 on 2021-09-08 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestorPedidos', '0003_auto_20210906_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='licitacion',
            field=models.ManyToManyField(to='gestorPedidos.Licitacion'),
        ),
        migrations.AlterField(
            model_name='licitacion',
            name='fecha_apertura',
            field=models.CharField(max_length=30),
        ),
    ]
