# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from os.path import join

from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFit, ResizeToFill


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Show(BaseModel):
    # Fields
    name = models.CharField(_(u"Name"), max_length=100)
    logo_original = models.ImageField(_(u"Logo"),
                                      upload_to=join("shows", "logos"))
    card_original = models.ImageField(_(u"Card"),
                                      upload_to=join("shows", "cards"))

    # Thumbnails
    logo = ImageSpecField(source='logo_original',
                          processors=[ResizeToFit(150, 70)],
                          format='PNG', options={'quality': 60})

    card = ImageSpecField(source='card_original',
                          processors=[ResizeToFill(200, 324)],
                          format='JPEG', options={'quality': 60})