# Generated by Django 5.1 on 2024-08-14 08:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repairjob',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='repairjob',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='license_plate',
        ),
        migrations.AddField(
            model_name='repairjob',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2024, 8, 14, 8, 27, 42, 193948, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='repairjob',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2024, 8, 14, 8, 27, 55, 953201, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='repairjob',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='repairjob',
            name='status',
            field=models.CharField(choices=[('pending', '待機中'), ('in_progress', '進行中'), ('completed', '完了')], default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='make',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='model',
            field=models.CharField(max_length=100),
        ),
    ]
