# Generated by Django 4.2.7 on 2024-01-24 10:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0005_user_followers_alter_blog_publish_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followers',
        ),
        migrations.AlterField(
            model_name='blog',
            name='caption',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 24, 10, 26, 13, 119165, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 24, 10, 26, 13, 119386, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2024, 1, 24, 10, 26, 13, 118124, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
