from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from match.models import Team, Match


@receiver(post_save, sender=Match)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        mathcesPlayedByPlayer(instance.team1.team_players.all())
        mathcesPlayedByPlayer(instance.team2.team_players.all())
        instance.winner.points += 1
        instance.winner.save()


def mathcesPlayedByPlayer(players):
    for player in players:
        player.totalMatch += 1
        player.save()


@receiver(post_delete, sender=Match)
def save_user_profile(sender, instance, **kwargs):
    instance.winner.points -= 1
    instance.winner.save()