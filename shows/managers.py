# -*- encoding: utf-8 -*-
from django.db.models import Manager


class PublishedManager(Manager):
    def get_queryset(self):
        qs = super(PublishedManager, self).get_queryset()
        return qs.filter(published=True)