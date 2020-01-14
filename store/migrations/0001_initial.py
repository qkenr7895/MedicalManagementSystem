# Generated by Django 2.2.7 on 2019-12-11 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0001_initial'),
        ('account', '0001_initial'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('s_name', models.CharField(default=0, max_length=500)),
                ('s_address', models.CharField(default=0, max_length=500)),
                ('s_latitude', models.CharField(default=0, max_length=500)),
                ('s_longitude', models.CharField(default=0, max_length=500)),
                ('s_type', models.CharField(default=0, max_length=500)),
                ('s_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Account')),
            ],
        ),
        migrations.CreateModel(
            name='ReservationStore',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('r_date', models.CharField(max_length=500)),
                ('r_time', models.CharField(default=0, max_length=500)),
                ('r_type', models.CharField(default='확인중', max_length=500)),
                ('r_patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient.Patient')),
                ('r_prescription', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.Prescription')),
                ('r_store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Store')),
            ],
        ),
    ]