from django.contrib import admin
from . import models

@admin.register(models.Server)
@admin.register(models.Characteristic)
@admin.register(models.Ornament)
@admin.register(models.Title)
@admin.register(models.Emote)
@admin.register(models.Spell)
@admin.register(models.SpellLevel)
@admin.register(models.SpellState)
@admin.register(models.CharacterClass)

class ServerAdmin(admin.ModelAdmin):
    pass
