# Generated by Django 5.0.4 on 2024-05-12 10:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_comment_time_stamp_alter_confession_time_stamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_stamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='confession',
            name='time_stamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
