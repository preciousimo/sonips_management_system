# Generated by Django 4.1.3 on 2023-02-22 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('due_date', models.DateTimeField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
