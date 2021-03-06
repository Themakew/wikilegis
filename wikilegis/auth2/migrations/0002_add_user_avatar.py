# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
import image_cropping.fields
import wikilegis.auth2.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=image_cropping.fields.ImageCropField(
                blank=True, null=True,
                upload_to='avatars/',
                validators=[wikilegis.auth2.models.avatar_validation]),
        ),
        migrations.AddField(
            model_name='user',
            name=b'cropping',
            field=image_cropping.fields.ImageRatioField(
                'avatar',
                '70x70',
                hide_image_field=False,
                size_warning=False,
                allow_fullsize=False,
                free_crop=False,
                adapt_rotation=False,
                help_text=None,
                verbose_name='cropping'),
        ),
    ]
