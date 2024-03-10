# Generated by Django 4.2.7 on 2024-01-31 12:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0011_alter_blog_authorid_alter_blog_publish_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 31, 12, 49, 56, 314537, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 31, 12, 49, 56, 314764, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2024, 1, 31, 12, 49, 56, 313477, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
