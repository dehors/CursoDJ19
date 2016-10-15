# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20161014_2305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='contenttypes',
            new_name='content',
        ),
    ]
