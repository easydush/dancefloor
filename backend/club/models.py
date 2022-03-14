from django.db import models
from django.utils.translation import gettext_lazy as _

DEFAULT_CHAR_MAX_LENGTH = 64


class Action(models.TextChoices):
    DRINK = 'DRINK', _('is drinking')
    DANCE = 'DANCE', _('is dancing')
    STOP = 'STOP', _('is stopping')


class Level(models.TextChoices):
    LOW = ('LOW', 'likes')
    MEDIUM = ('MEDIUM', 'is good in')
    HIGH = ('HIGH', 'is professional in')

class Dance(models.Model):
    style = models.CharField(
        max_length=DEFAULT_CHAR_MAX_LENGTH,
        blank=False,
        unique=True
    )
    body = models.CharField(
        max_length=DEFAULT_CHAR_MAX_LENGTH, blank=False)
    head = models.CharField(
        max_length=DEFAULT_CHAR_MAX_LENGTH, blank=False)
    hands = models.CharField(
        max_length=DEFAULT_CHAR_MAX_LENGTH, blank=False)
    legs = models.CharField(
        max_length=DEFAULT_CHAR_MAX_LENGTH, blank=False)

    def __str__(self):
        return f'{self.style}: head is {self.head}, body is {self.body}, ' \
               f'hands are {self.hands}, legs are {self.legs},'


class Dancer(models.Model):
    name = models.CharField(max_length=DEFAULT_CHAR_MAX_LENGTH, blank=False,
                            unique=True)
    sex = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def action(self, style=None):
        if not style:
            return Action.STOP
        can_dance = str(style) in list(self.skills.values_list('dance__style', flat=True))
        return Action.DANCE if can_dance else Action.DRINK

    def current_skill(self, style=None):
        if not style:
            return 'is stopped'
        can_dance = str(style) in list(self.skills.values_list('dance__style', flat=True))
        if not can_dance:
            return 'is drinking'
        return self.skills.filter(dance__style=style).first().get_movement()


class DanceSkill(models.Model):
    dancer = models.ForeignKey(Dancer, on_delete=models.CASCADE, related_name='skills')
    dance = models.ForeignKey(Dance, on_delete=models.CASCADE, related_name='dancers')
    level = models.CharField(max_length=10, choices=Level.choices, blank=False)

    def __str__(self):
        return f'{self.dancer.name} {self.level} {self.dance.style}'

    def get_style_label(self):
        return Level(self.level).label

    def get_movement(self):
        return f'{self.get_style_label()} {str(self.dance)}'
