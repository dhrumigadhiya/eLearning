# Generated by Django 5.0.1 on 2024-04-16 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS', '0019_alter_tblstuquery_isactive_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbladminlogin',
            name='username',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tblempcourse',
            name='ContactNo',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='tblempcourse',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tblempdetails',
            name='ContactNo',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='tblempdetails',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tbllogin',
            name='Password',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='tblstucourse',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tblstudentregistration',
            name='email',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='tblstudentregistration',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tblstuquery',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]