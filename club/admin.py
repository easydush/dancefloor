from django.contrib import admin

from club.models import Dancer, DanceSkill


@admin.register(Dancer, DanceSkill)
class DancerAdmin(admin.ModelAdmin):
    pass