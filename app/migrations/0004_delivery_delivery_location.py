# Generated by Django 2.2.6 on 2019-10-23 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191021_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='delivery_location',
            field=models.CharField(choices=[('home', 'Home'), ('health_facility', 'Health Facility')], default='home', max_length=250),
        ),
    ]
