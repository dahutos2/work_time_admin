# Generated by Django 3.2.6 on 2021-09-24 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_time', '0002_worktime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worktime',
            name='summary',
        ),
        migrations.AlterField(
            model_name='worktime',
            name='description',
            field=models.TextField(blank=True, verbose_name='メモ'),
        ),
    ]
