# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0005_auto_20150411_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='type',
            field=models.CharField(default=b'G', max_length=1, choices=[(b'H', b'Hybrid'), (b'G', b'Gas'), (b'E', b'Electric')]),
            preserve_default=True,
        ),
    ]
