# Generated by Django 3.2.5 on 2021-07-08 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_monitoring', '0004_auto_20210708_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu',
            name='frequency',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='percent_usage',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='disks',
            name='percent_used',
            field=models.IntegerField(),
        ),
    ]