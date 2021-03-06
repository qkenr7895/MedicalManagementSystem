# Generated by Django 2.2.7 on 2019-12-11 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=100)),
                ('p_phone', models.CharField(max_length=100)),
                ('p_latitude', models.CharField(max_length=100)),
                ('p_longitude', models.CharField(max_length=100)),
                ('p_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('f_hospital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.Hospital')),
                ('f_patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patient.Patient')),
            ],
        ),
    ]
