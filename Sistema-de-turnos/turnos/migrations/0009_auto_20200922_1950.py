# Generated by Django 3.1 on 2020-09-22 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0008_auto_20200922_1428'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turno',
            old_name='dias',
            new_name='horas',
        ),
    ]