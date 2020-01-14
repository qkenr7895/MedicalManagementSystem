# Generated by Django 2.2.7 on 2019-12-11 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('h_key', models.CharField(max_length=200)),
                ('h_name', models.CharField(max_length=200)),
                ('h_latitude', models.CharField(max_length=50)),
                ('h_longitude', models.CharField(max_length=50)),
                ('h_address', models.CharField(max_length=550)),
                ('h_specialCount', models.CharField(max_length=10)),
                ('h_open1', models.CharField(default='09:00', max_length=10)),
                ('h_close1', models.CharField(default='17:00', max_length=10)),
                ('h_open2', models.CharField(default='09:00', max_length=10)),
                ('h_close2', models.CharField(default='17:00', max_length=10)),
                ('h_open3', models.CharField(default='09:00', max_length=10)),
                ('h_close3', models.CharField(default='17:00', max_length=10)),
                ('h_open4', models.CharField(default='09:00', max_length=10)),
                ('h_close4', models.CharField(default='17:00', max_length=10)),
                ('h_open5', models.CharField(default='09:00', max_length=10)),
                ('h_close5', models.CharField(default='17:00', max_length=10)),
                ('h_open6', models.CharField(default='09:00', max_length=10)),
                ('h_close6', models.CharField(default='17:00', max_length=10)),
                ('h_open7', models.CharField(default='09:00', max_length=10)),
                ('h_close7', models.CharField(default='17:00', max_length=10)),
                ('h_medicalCourse', models.CharField(default='[false, false, false, false, false, false, false, false, false, false,                         false, false, false, false, false, false, false, false, false, false,                         false, false, false, false, false, false, false, false, false, false,                         false, false, false, false, false, false, false, false, false, false,                         false, false, false, false, false, false, false, false, false, false,                         false, false, false, false, false, false, false, false, false, false,                         false, false, false, false, false, false, false, false, false, false,                         false, false, false, false, false, false, false, false, false, false,                         false, false, false, false, false, false, false, false, false, false, false]', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(default='none', max_length=500)),
                ('p_phone', models.CharField(default='none', max_length=500)),
                ('p_date', models.CharField(max_length=500)),
                ('p_time', models.CharField(default=0, max_length=500)),
                ('p_else', models.CharField(default='none', max_length=5000)),
                ('p_medicine1', models.CharField(default='none', max_length=100)),
                ('p_dosage1', models.CharField(default='none', max_length=100)),
                ('p_dosageCount1', models.CharField(default='none', max_length=100)),
                ('p_totalDosage1', models.CharField(default='none', max_length=100)),
                ('p_medicine2', models.CharField(default='none', max_length=100)),
                ('p_dosage2', models.CharField(default='none', max_length=100)),
                ('p_dosageCount2', models.CharField(default='none', max_length=100)),
                ('p_totalDosage2', models.CharField(default='none', max_length=100)),
                ('p_medicine3', models.CharField(default='none', max_length=100)),
                ('p_dosage3', models.CharField(default='none', max_length=100)),
                ('p_dosageCount3', models.CharField(default='none', max_length=100)),
                ('p_totalDosage3', models.CharField(default='none', max_length=100)),
                ('p_medicine4', models.CharField(default='none', max_length=100)),
                ('p_dosage4', models.CharField(default='none', max_length=100)),
                ('p_dosageCount4', models.CharField(default='none', max_length=100)),
                ('p_totalDosage4', models.CharField(default='none', max_length=100)),
                ('p_complete_date', models.CharField(default='none', max_length=500)),
                ('p_complete_time', models.CharField(default='none', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('r_date', models.CharField(max_length=500)),
                ('r_time', models.CharField(default=0, max_length=500)),
                ('r_hospital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.Hospital')),
            ],
        ),
    ]