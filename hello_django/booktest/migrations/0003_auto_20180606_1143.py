# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_auto_20180606_1138'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='bookinfo',
            table='booktest_bookinfo',
        ),
        migrations.AlterModelTable(
            name='heroinfo',
            table='booktest_heroinfo',
        ),
    ]
