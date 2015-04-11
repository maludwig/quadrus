# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(default=1, upload_to=b'vehicles'),
            preserve_default=False,
        ),
    ]
