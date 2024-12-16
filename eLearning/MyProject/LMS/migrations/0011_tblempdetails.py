# Generated by Django 5.0.1 on 2024-03-07 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS', '0010_tblstuquery'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblEmpDetails',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=600)),
                ('ContactNo', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=100)),
                ('Designation', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=30)),
                ('Createdate', models.DateField(auto_now=True)),
                ('Modifydate', models.DateField(auto_now=True)),
                ('Modifyby', models.CharField(max_length=50)),
                ('isActive', models.BooleanField(default=False)),
                ('isDeactive', models.BooleanField(default=False)),
            ],
        ),
    ]
