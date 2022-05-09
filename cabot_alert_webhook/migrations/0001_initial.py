# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cabotapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebhookAlert',
            fields=[
                ('alertplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cabotapp.AlertPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cabotapp.alertplugin',),
        ),
        migrations.CreateModel(
            name='WebhookAlertUserData',
            fields=[
                ('alertpluginuserdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cabotapp.AlertPluginUserData')),
                ('webhook_url', models.URLField(blank=True, max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=('cabotapp.alertpluginuserdata',),
        ),
    ]
