# Generated by Django 5.0.1 on 2024-04-04 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS', '0018_alter_tblstuquery_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblstuquery',
            name='isActive',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='tblstuquery',
            name='isCompleted',
            field=models.BooleanField(default=False, null=True),
        ),
    ]