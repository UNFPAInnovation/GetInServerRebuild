# Generated by Django 2.2.6 on 2019-11-04 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0047_auto_20191102_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='followup',
            name='anc_card',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='followup',
            name='follow_up_reason',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='followup',
            name='missed_anc_reason',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='girl',
            name='marital_status',
            field=models.CharField(choices=[('Married', 'Married'), ('Single', 'Single'), ('Divorced', 'Divorced')], default='Single', max_length=250),
        ),
    ]