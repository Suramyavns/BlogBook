# Generated by Django 4.2.7 on 2024-02-20 12:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0019_follower_follower_follower_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 20, 12, 47, 6, 615907, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 20, 12, 47, 6, 616154, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='replies',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 20, 12, 47, 6, 616366, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2024, 2, 20, 12, 47, 6, 614869, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
