# Generated by Django 2.2.6 on 2019-11-06 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0065_auto_20191106_0757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='next_appointment',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='girl',
            name='marital_status',
            field=models.CharField(choices=[('Married', 'Married'), ('Single', 'Single'), ('Divorced', 'Divorced')], default='Single', max_length=250),
        ),
    ]
