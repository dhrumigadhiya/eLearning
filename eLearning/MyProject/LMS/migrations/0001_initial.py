# Generated by Django 4.2.4 on 2024-01-30 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tblStudentRegistration',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('mobileno', models.CharField(max_length=15)),
                ('Course', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=600)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('Password', models.CharField(max_length=30)),
                ('regdate1', models.DateField(auto_now=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='IMG/')),
                ('isActive', models.BooleanField(default=False)),
            ],
        ),
    ]
