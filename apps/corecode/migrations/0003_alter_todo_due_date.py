# Generated by Django 4.1.3 on 2023-02-22 13:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0002_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
