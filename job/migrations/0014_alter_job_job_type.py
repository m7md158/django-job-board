# Generated by Django 5.1 on 2024-09-03 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0013_alter_job_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Part Time', 'Part Time'), ('Full Time', 'Full Time')], max_length=15),
        ),
    ]
