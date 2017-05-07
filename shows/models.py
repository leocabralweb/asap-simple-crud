# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import timedelta
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from os.path import join

from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFit, ResizeToFill

from shows import managers


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Show(BaseModel):
    # Fields
    published = models.BooleanField(_(u"Published"), default=False)
    name = models.CharField(_(u"Name"), max_length=100)
    logo_original = models.ImageField(_(u"Logo"),
                                      upload_to=join("shows", "logos"))
    card_original = models.ImageField(_(u"Card"),
                                      upload_to=join("shows", "cards"))
    duration = models.DurationField(_(u"Duration"),
                                    default=timedelta(minutes=30))


    # Thumbnails
    logo = ImageSpecField(source='logo_original',
                          processors=[ResizeToFit(150, 70)],
                          format='PNG', options={'quality': 60})

    card = ImageSpecField(source='card_original',
                          processors=[ResizeToFill(200, 324)],
                          format='JPEG', options={'quality': 60})

    # Custom Managers
    object = models.Manager()
    available = managers.PublishedManager()

    def __unicode__(self):
        return self.name


class Schedule(BaseModel):
    show = models.ForeignKey("Show", related_name="schedule")
    start = models.DateTimeField(_(u"Start"))
    end = models.DateTimeField(_(u"End"), blank=True,
                               help_text=_(u"Leave blank to automatic fill."))

@receiver(pre_save, sender=Schedule)
def calculate_schedule_end(sender, instance, **kwargs):
    if not instance.end:
        instance.end = instance.start + instance.show.duration