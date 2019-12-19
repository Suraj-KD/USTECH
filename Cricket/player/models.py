# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from common.models import Country
from match.models import Team

# Create your models here.
class Player(models.Model):
    """Docstring for Player"""
    fname = models.CharField(max_length=100, blank=False, null=False)
    lname = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='players_image/', blank=True)
    jourseyNumber = models.CharField(max_length=100, blank=True, null=True)
    country = models.ForeignKey(Country, related_name='country_players', on_delete=models.CASCADE)
    hundreds = models.PositiveIntegerField(default=0)
    fifties = models.PositiveIntegerField(default=0)
    highestScore = models.PositiveIntegerField(default=0)
    totalMatch = models.PositiveIntegerField(default=0)
    team = models.ForeignKey(Team, related_name='team_players', null=True)

    def __str__(self):
        return "{} {} - {}".format(self.fname, self.lname, self.country.name)

    def get_full_name(self):
        if self.fname and self.lname:
            fullname = "{} {}".format(self.fname, self.lname)
        elif self.fname:
            fullname = "{}".format(self.fname)
        elif self.lname:
            fullname = "{}".format(self.lname)
        else:
            fullname = "NA"
        return fullname
