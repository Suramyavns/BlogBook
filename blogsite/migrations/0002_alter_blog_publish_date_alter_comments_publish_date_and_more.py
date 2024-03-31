# Generated by Django 4.2.7 on 2024-03-31 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 31, 14, 31, 47, 242607, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 31, 14, 31, 47, 242855, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='replies',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 31, 14, 31, 47, 243072, tzinfo=datetime.timezone.utc)),
        ),
    ]