# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Country(models.Model):
    """docstring for Country"""
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name


class State(models.Model):
    """docstring for State"""
    name = models.CharField(max_length=100, blank=False, null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.name, self.country.name)
