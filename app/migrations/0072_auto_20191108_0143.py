# Generated by Django 2.2.6 on 2019-11-08 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0071_auto_20191108_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='girl',
            name='marital_status',
            field=models.CharField(choices=[('Divorced', 'Divorced'), ('Married', 'Married'), ('Single', 'Single')], default='Single', max_length=250),
        ),
    ]
