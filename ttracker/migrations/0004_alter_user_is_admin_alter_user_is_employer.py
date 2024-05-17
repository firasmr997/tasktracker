# Generated by Django 5.0.2 on 2024-05-15 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttracker', '0003_employeur_task_penalite_employeurtask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Manager'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_employer',
            field=models.BooleanField(default=True, verbose_name='Employee'),
        ),
    ]
