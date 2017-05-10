# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 00:15
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(default=uuid.uuid1, max_length=512)),
                ('groups', models.ManyToManyField(related_name='inventories', to='main.Group')),
                ('hosts', models.ManyToManyField(related_name='inventories', to='main.Host')),
            ],
            options={
                'default_related_name': 'inventories',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='children',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='group',
            name='groups',
            field=models.ManyToManyField(blank=True, null=True, related_name='_group_groups_+', to='main.Group'),
        ),
    ]