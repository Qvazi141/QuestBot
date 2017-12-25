# Generated by Django 2.0 on 2017-12-24 20:13

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20171224_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='handler',
            name='enabled_on',
        ),
        migrations.AddField(
            model_name='handler',
            name='on_button_click',
            field=models.BooleanField(default=False, verbose_name='Enabled on button click'),
        ),
        migrations.AddField(
            model_name='handler',
            name='on_callback_msg',
            field=models.BooleanField(default=False, verbose_name='Enabled on callback message'),
        ),
        migrations.AddField(
            model_name='handler',
            name='on_common_msg',
            field=models.BooleanField(default=False, verbose_name='Enabled on common message'),
        ),
        migrations.AlterField(
            model_name='event',
            name='send_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 24, 20, 13, 0, 43328, tzinfo=utc), verbose_name='Time to send on'),
        ),
    ]
