# Generated by Django 2.2.6 on 2019-10-25 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20191025_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='mappingencounter',
            name='voucher_card',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='girl',
            name='marital_status',
            field=models.CharField(choices=[('divorced', 'Divorced'), ('married', 'Married'), ('single', 'Single')], default='single', max_length=250),
        ),
    ]