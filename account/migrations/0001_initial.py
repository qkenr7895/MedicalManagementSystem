# Generated by Django 2.2.7 on 2019-12-11 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('a_local', models.CharField(max_length=100)),
                ('a_domain', models.CharField(max_length=100)),
                ('a_password', models.CharField(max_length=100)),
            ],
        ),
    ]
