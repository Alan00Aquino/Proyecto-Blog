# Generated by Django 4.2.3 on 2023-08-03 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_remove_usuario_domicilio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='es_miembro',
            field=models.BooleanField(default=True),
        ),
    ]
