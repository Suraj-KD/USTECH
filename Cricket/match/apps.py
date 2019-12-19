# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class MatchConfig(AppConfig):
    name = 'match'

    def ready(self):
        import match.signals
