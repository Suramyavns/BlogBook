# Generated by Django 4.2.7 on 2024-02-19 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0015_alter_blog_publish_date_alter_comments_publish_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(default='blank.webp', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 19, 12, 57, 2, 945613, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 19, 12, 57, 2, 945858, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='replies',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 19, 12, 57, 2, 946070, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2024, 2, 19, 12, 57, 2, 944522, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
