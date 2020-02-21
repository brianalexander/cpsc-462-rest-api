from django.db import models
from django.conf import settings
from uuid import uuid4


class TicTacToe(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    winner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name='tictactoe_winner',
        on_delete=models.SET_NULL)
    players = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='tictactoe_games')
    game_code = models.UUIDField(
        default=uuid4,
        editable=False,
        null=False)
    state = models.TextField()
