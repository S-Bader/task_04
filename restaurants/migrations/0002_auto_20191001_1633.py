# Generated by Django 2.1.5 on 2019-10-01 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='closing_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='opening_time',
            field=models.TimeField(),
        ),
    ]
