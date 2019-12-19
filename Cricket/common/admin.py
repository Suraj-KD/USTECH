# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Country, State

# Register your models here.
admin.site.register(Country)
admin.site.register(State)