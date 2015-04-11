# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_vehicle_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_date', models.DateTimeField()),
                ('completed', models.BooleanField(default=False)),
                ('built_date', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(to='vehicles.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='vehicle',
            field=models.ForeignKey(to='vehicles.Vehicle'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='make',
            field=models.CharField(default=b'Lexus', max_length=200),
        ),
    ]
