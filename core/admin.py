from django.contrib import admin

from core import models


# Register your models here.

@admin.register(models.Player)
class Player(admin.ModelAdmin):
    list_display = ['id', 'name', 'birth_date', 'position']
    list_display_links = ['id', 'name', 'birth_date', 'position']

@admin.register(models.Club)
class Club(admin.ModelAdmin):
    list_display = ['id', 'name', 'badge']
    list_display_links = ['id', 'name', 'badge']

@admin.register(models.Championship)
class Championship(admin.ModelAdmin):
    list_display = ['id', 'description', 'start_date', 'end_date']
    list_display_links = ['id', 'description', 'start_date', 'end_date']

@admin.register(models.PlayerStatistics)
class PlayerStatistics(admin.ModelAdmin):
    list_display = ['id', 'yellow_cards', 'red_cards', 'goals', 'shirt_number']
    list_display_links = ['id', 'yellow_cards', 'red_cards', 'goals', 'shirt_number']

@admin.register(models.ClubStatistics)
class ClubStatistics (admin.ModelAdmin):
    list_display = ['id', 'wins', 'losses', 'draws', 'goals_for', 'goals_against','yellow_cards','red_cards' , 'walkover']
    list_display_links = ['id', 'wins', 'losses', 'draws', 'goals_for', 'goals_against','yellow_cards','red_cards' , 'walkover']

@admin.register(models.Matches)
class Matches(admin.ModelAdmin):
    list_display = ['id', 'date', 'time', 'location', 'penalty1', 'penalty2']
    list_display_links = ['id', 'date', 'time', 'location', 'penalty1', 'penalty2']


@admin.register(models.MatchClub)
class MatchClub(admin.ModelAdmin):
    list_display = ['id', 'goals']
    list_display_links = ['id', 'goals']
