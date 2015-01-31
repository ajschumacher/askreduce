# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('user', models.CharField(max_length=32)),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('user', models.CharField(max_length=32)),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='shufflesort.Question'),
            preserve_default=True,
        ),
    ]
