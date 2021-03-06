# Generated by Django 2.2.6 on 2019-11-14 21:50

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('role', models.CharField(choices=[('developer', 'developer'), ('dho', 'dho'), ('chew', 'chew'), ('midwife', 'midwife'), ('ambulance', 'ambulance')], default='developer', help_text='developer - Developer, dho - DHO, chew - CHEW, midwife - Midwife, ambulance - Ambulance, manager - Manager', max_length=50)),
                ('phone', models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(message='Wrong phone number format', regex='^(07)[0-9]{8}$')])),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='female', help_text='male - Male, female - Female', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('number_plate', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Missed', 'Missed'), ('Attended', 'Attended'), ('Expected', 'Expected')], default='Expected', max_length=250)),
                ('odk_instance_id', models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
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
            name='FamilyPlanning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pre', 'Pre'), ('Post', 'Post')], default='Pre', max_length=250)),
                ('method', models.CharField(blank=True, max_length=250, null=True)),
                ('no_family_planning_reason', models.CharField(blank=True, max_length=250, null=True)),
                ('using_family_planning', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Girl',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('phone_number', models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator(message='Wrong phone number format', regex='^(07)[0-9]{8}$')])),
                ('trimester', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1)])),
                ('next_of_kin_phone_number', models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator(message='Wrong phone number format', regex='^(07)[0-9]{8}$')])),
                ('education_level', models.CharField(choices=[('Primary level', 'Primary Level'), ('O level', 'O Level'), ('A level', 'A Level'), ('Tertiary', 'Tertiary Level')], default='Primary level', max_length=250)),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Single', 'Single'), ('Divorced', 'Divorced')], default='Single', max_length=250)),
                ('last_menstruation_date', models.DateField()),
                ('dob', models.DateField()),
                ('age', models.IntegerField(blank=True, null=True)),
                ('pending_visits', models.IntegerField(default=30, validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(0)])),
                ('missed_visits', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(0)])),
                ('completed_all_visits', models.BooleanField(blank=True, default=False, null=True)),
                ('odk_instance_id', models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blurred_vision', models.BooleanField(default=False)),
                ('bleeding_heavily', models.BooleanField(default=False)),
                ('fever', models.BooleanField(default=False)),
                ('swollen_feet', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Parish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('parish', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Parish')),
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
        migrations.CreateModel(
            name='SmsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=400, null=True)),
                ('message_id', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('sender_id', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('girl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Girl')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='parish',
            name='sub_county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.SubCounty'),
        ),
        migrations.CreateModel(
            name='MappingEncounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucher_card', models.CharField(blank=True, max_length=250, null=True)),
                ('attended_anc_visit', models.BooleanField(default=False)),
                ('odk_instance_id', models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('family_planning', models.ManyToManyField(blank=True, null=True, to='app.FamilyPlanning')),
                ('girl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Girl')),
                ('observation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Observation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='HealthFacility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('parish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Parish')),
            ],
        ),
        migrations.AddField(
            model_name='girl',
            name='village',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Village'),
        ),
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_up_action_taken', models.CharField(blank=True, max_length=400, null=True)),
                ('odk_instance_id', models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('girl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Girl')),
                ('observation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Observation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_taken', models.CharField(max_length=200)),
                ('postnatal_care', models.BooleanField(default=True)),
                ('mother_alive', models.BooleanField(default=True)),
                ('baby_alive', models.BooleanField(default=True)),
                ('baby_death_date', models.DateTimeField(blank=True, null=True)),
                ('baby_birth_date', models.DateTimeField(blank=True, null=True)),
                ('mother_death_date', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('delivery_location', models.CharField(choices=[('Home', 'Home'), ('Health facility', 'Health Facility')], default='Home', max_length=250)),
                ('odk_instance_id', models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('family_planning', models.ManyToManyField(blank=True, null=True, to='app.FamilyPlanning')),
                ('girl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Girl')),
                ('health_facility', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.HealthFacility')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='county',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.District'),
        ),
        migrations.CreateModel(
            name='AppointmentEncounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('needed_ambulance', models.BooleanField(default=False)),
                ('missed_anc_before', models.BooleanField(default=False)),
                ('used_ambulance', models.BooleanField(default=False)),
                ('missed_anc_reason', models.CharField(blank=True, max_length=250, null=True)),
                ('action_taken', models.CharField(blank=True, max_length=250, null=True)),
                ('appointment_method', models.CharField(blank=True, max_length=250, null=True)),
                ('odk_instance_id', models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Appointment')),
                ('observation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Observation')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='appointment',
            name='girl',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Girl'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='health_facility',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.HealthFacility'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.District'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='midwife',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='user',
            name='village',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Village'),
        ),
    ]
