# Generated by Django 4.2.7 on 2024-02-06 13:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0014_remove_comments_replyids_alter_blog_publish_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 6, 13, 11, 28, 96954, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 6, 13, 11, 28, 97187, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2024, 2, 6, 13, 11, 28, 95907, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.CreateModel(
            name='replies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('publish_date', models.DateField(default=datetime.datetime(2024, 2, 6, 13, 11, 28, 97415, tzinfo=datetime.timezone.utc))),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('authorid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogsite.comments')),
            ],
        ),
    ]