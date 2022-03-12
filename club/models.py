from django.db import models
from django.utils.translation import gettext_lazy as _

DEFAULT_CHAR_MAX_LENGTH = 64


class Action(models.TextChoices):
    DRINK = 'DRINK', _('is drinking')
    DANCE = 'DANCE', _('is dancing')
    STOP = 'STOP', _('is stopping')


class Level(models.TextChoices):
    LOW = 'LOW', _('likes')
    MEDIUM = 'MEDIUM', _('is good in')
    HIGH = 'HIGH', _('is professional in')


class DanceStyle(models.TextChoices):
    RNB = 'RNB', _('RnB')
    HIPHOP = 'HIPHOP', _('hip-hop')
    ELECTRODANCE = 'ELECTRODANCE', _('electrodance')
    HOUSE = 'HOUSE', _('house')
    POP = 'POP', _('pop')


class Dancer(models.Model):
    name = models.CharField(max_length=DEFAULT_CHAR_MAX_LENGTH, blank=False)
    sex = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class DanceSkill(models.Model):
    dancer = models.ForeignKey(Dancer, on_delete=models.CASCADE)
    level = models.CharField(
        max_length=10,
        choices=Level.choices,
        blank=False
    )

    style = models.CharField(
        max_length=DEFAULT_CHAR_MAX_LENGTH,
        choices=DanceStyle.choices,
        blank=False
    )

    def __str__(self):
        return f'{self.dancer.name} {self.level} {self.style}'
