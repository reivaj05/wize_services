# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshort',
            name='short_url',
            field=models.CharField(help_text='Insert Url to convert', max_length=200, verbose_name='Short url'),
        ),
    ]
