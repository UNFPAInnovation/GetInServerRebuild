# Generated by Django 2.2.6 on 2019-10-25 11:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20191023_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='girl',
            old_name='next_of_kin_name',
            new_name='next_of_kin_first_name',
        ),
        migrations.AddField(
            model_name='girl',
            name='next_of_kin_last_name',
            field=models.CharField(default='Sharon', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='girl',
            name='marital_status',
            field=models.CharField(choices=[('married', 'Married'), ('single', 'Single'), ('divorced', 'Divorced')], default='single', max_length=250),
        ),
        migrations.AlterField(
            model_name='girl',
            name='trimester',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1)]),
        ),
    ]
