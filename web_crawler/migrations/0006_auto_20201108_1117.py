# Generated by Django 3.1.2 on 2020-11-08 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_crawler', '0005_auto_20201108_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='price',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='time',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
