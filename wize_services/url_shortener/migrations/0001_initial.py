# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlShort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('long_url', models.URLField(help_text='Insert Url to convert', verbose_name='Long url')),
                ('short_url', models.URLField(help_text='Insert Url to convert', verbose_name='Short url')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
