# Generated by Django 2.2.6 on 2019-10-21 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20191021_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='baby_birth_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='baby_death_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='mother_death_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
