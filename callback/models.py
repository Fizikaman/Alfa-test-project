from django.db import models


class Player(models.Model):
    name = models.CharField(
        max_length=54,
        verbose_name="Игрок",
        unique=True,
    )
    email = models.EmailField(
        max_length=54,
        verbose_name="Эл почта",
        unique=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата изменения",
    )


class Game(models.Model):
    name = models.CharField(
        max_length=254,
        default=""
    )
    players = models.ManyToManyField(
        Player,
        blank=True,
        on_delete=models.PROTECT,
        related_name='games',
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата изменения",
    )
