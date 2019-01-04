# Generated by Django 2.1.4 on 2019-01-04 02:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190103_2245'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='despesa',
            options={'ordering': ('-vencimento', 'forma_pagamento'), 'verbose_name': 'Despesa', 'verbose_name_plural': 'Despesas'},
        ),
        migrations.AddField(
            model_name='despesa',
            name='data_atual',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 4, 0, 23, 34, 691992)),
        ),
    ]
