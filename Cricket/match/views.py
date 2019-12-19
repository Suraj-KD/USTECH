# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db import IntegrityError
from match.models import Team, Match

# Create your views here.
def index(request):
    context_dict = {}
    allteam = Team.objects.all()
    context_dict['teams'] = allteam
    context_dict['matches'] = Match.objects.all()[:10]
    return render(request, 'match/main.html', context_dict)

def team_details(request, team_id):
    try:
        team = Team.objects.get(pk=team_id)
        players = team.team_players.all()
        context_dict = {}
        context_dict['players'] = players
        context_dict['team'] = team
        return render(request, 'player/players.html', context_dict)
    except IntegrityError:
        pass
