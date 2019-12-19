# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now
from common.models import State

# Create your models here.
class Team(models.Model):
    """Docstring for Team"""
    name = models.CharField(max_length=100, blank=False, null=False)
    logoURI = models.ImageField(upload_to='team/')
    clubState = models.ForeignKey(State, on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "{} - {}".format(self.name, self.clubState.name)


class Match(models.Model):
    """Docstring for Team"""
    team1 = models.ForeignKey(Team, related_name='%(class)s_team1')
    team2 = models.ForeignKey(Team, related_name='%(class)s_team2')
    winner = models.ForeignKey(Team, related_name='winner')
    date = models.DateField(default=now)

    def __str__(self):
        return "Between {} and {}".format(self.team1, self.team2)