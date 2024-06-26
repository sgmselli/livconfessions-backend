# Generated by Django 5.0.4 on 2024-05-13 12:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_comment_downvotes_remove_comment_upvotes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='downvotes',
            field=models.ManyToManyField(blank=True, related_name='comment_downvotes', to='base.userkey'),
        ),
        migrations.AddField(
            model_name='comment',
            name='upvotes',
            field=models.ManyToManyField(blank=True, related_name='comment_upvotes', to='base.userkey'),
        ),
        migrations.AddField(
            model_name='confession',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='comments', to='base.comment'),
        ),
        migrations.AddField(
            model_name='confession',
            name='downvotes',
            field=models.ManyToManyField(blank=True, related_name='downvotes', to='base.userkey'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time_stamp',
            field=models.CharField(default=datetime.datetime(2024, 5, 13, 13, 39, 49, 638912), max_length=100),
        ),
        migrations.AlterField(
            model_name='confession',
            name='time_stamp',
            field=models.CharField(default=datetime.datetime(2024, 5, 13, 13, 39, 49, 639374), max_length=100),
        ),
    ]
