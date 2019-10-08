# Generated by Django 2.2.6 on 2019-10-08 09:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_dho'),
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Parish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Wrong phone number format', regex='^(07)[0-9]{8}$')]),
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('parish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Parish')),
            ],
        ),
        migrations.CreateModel(
            name='SubCounty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.County')),
            ],
        ),
        migrations.AddField(
            model_name='parish',
            name='sub_county',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.SubCounty'),
        ),
        migrations.CreateModel(
            name='Girl',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Wrong phone number format', regex='^(07)[0-9]{8}$')])),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Village')),
            ],
        ),
        migrations.AddField(
            model_name='county',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.District'),
        ),
    ]
