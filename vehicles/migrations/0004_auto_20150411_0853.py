# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_auto_20150411_0848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='vehicle',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
