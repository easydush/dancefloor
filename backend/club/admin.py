from django.contrib import admin

from club.models import Dancer, DanceSkill, Dance


@admin.register(Dancer, DanceSkill, Dance)
class DancerAdmin(admin.ModelAdmin):
    pass
