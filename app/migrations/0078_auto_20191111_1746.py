# Generated by Django 2.2.6 on 2019-11-11 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0077_auto_20191111_1739'),
    ]

    operations = [
        migrations.RenameField(
            model_name='smsmodel',
            old_name='sender',
            new_name='recipient',
        ),
        migrations.RemoveField(
            model_name='smsmodel',
            name='receiver',
        ),
        migrations.AddField(
            model_name='smsmodel',
            name='sender_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='girl',
            name='marital_status',
            field=models.CharField(choices=[('Divorced', 'Divorced'), ('Married', 'Married'), ('Single', 'Single')], default='Single', max_length=250),
        ),
    ]