# Generated by Django 2.2.6 on 2019-10-25 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20191025_1305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mappingencounter',
            old_name='bleeding',
            new_name='bleeding_heavily',
        ),
        migrations.AlterField(
            model_name='girl',
            name='marital_status',
            field=models.CharField(choices=[('single', 'Single'), ('divorced', 'Divorced'), ('married', 'Married')], default='single', max_length=250),
        ),
    ]