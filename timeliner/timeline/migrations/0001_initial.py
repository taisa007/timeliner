# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'followers',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Follows',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'follows',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('content', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField()),
            ],
            options={
                'db_table': 'tweets',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'users',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(to='timeline.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='follows',
            name='follow_user',
            field=models.ForeignKey(related_name='follows_follow_user', to='timeline.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='follows',
            name='user',
            field=models.ForeignKey(related_name='follows_user', to='timeline.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='followers',
            name='follower_user',
            field=models.ForeignKey(related_name='followers_follower_user', to='timeline.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='followers',
            name='user',
            field=models.ForeignKey(related_name='followers_user', to='timeline.User'),
            preserve_default=True,
        ),
    ]
