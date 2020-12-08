# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_reg_form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrainfo',
            name='allow_newsletter_emails',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
