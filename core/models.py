from django.db import models


class ModelBase(models.Model):
    id = models.AutoField(primary_key=True , null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    modified_at = models.DateTimeField(auto_now=True, null=False)
    active = models.BooleanField(default=True, null=False)

    class Meta:
        abstract = True
        managed = True

class Player(ModelBase):
    name = models.CharField(max_length=100, null=False)
    birth_date = models.DateField(null=False)
    position = models.CharField(max_length=100, null=False)
    class Meta:
        db_table = 'player'

class Club(ModelBase):
    name = models.CharField(max_length=100, null=False)
    badge = models.CharField(max_length=100, null=True, blank=True)
    class Meta:
        db_table = 'club'

class Championship(ModelBase):
    description = models.CharField(max_length=100, null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    class Meta:
        db_table = 'championship'

class PlayerStatistics(ModelBase):
    yellow_cards = models.IntegerField(null=True, blank=True)
    red_cards = models.IntegerField(null=True, blank=True)
    goals = models.IntegerField(null=False, blank=True)
    shirt_number = models.IntegerField(null=False, blank=True)

    id_championship = models.ForeignKey(
        to="Championship",
        on_delete=models.DO_NOTHING,
        db_column='id_championship',
        null=False,
        blank=False,
        related_name='player_statistics'
    )

    id_player = models.ForeignKey(
        to="Player",
        on_delete=models.DO_NOTHING,
        db_column='id_player',
        null=False,
        related_name='player_statistics',
        blank=False
    )
    class Meta:
        db_table = 'player_statistics'

class ClubStatistics(ModelBase):
    wins = models.IntegerField(null=False, blank=True)
    losses = models.IntegerField(null=False, blank=True)
    draws = models.IntegerField(null=False, blank=True)
    goals_for=models.IntegerField(null=False, blank=True)
    goals_against=models.IntegerField(null=False, blank=True)
    yellow_cards = models.IntegerField(null=False, blank=True)
    red_cards = models.IntegerField(null=False, blank=True)
    walkover = models.IntegerField(null=False, blank=True)
    id_club = models.ForeignKey(
        to="Club",
        on_delete=models.DO_NOTHING,
        db_column='id_club',
        null=False,
        blank=False,
        related_name='club_statistics'
    )
    id_championship = models.ForeignKey(
        to="Championship",
        on_delete=models.DO_NOTHING,
        db_column='id_championship',
        null=False,
        blank=False,
        related_name='club_statistics'
    )
    class Meta:
        db_table = 'club_statistics'

class Matches(ModelBase):
    date = models.DateField(null=False)
    time = models.TimeField(null=False)
    location = models.CharField(max_length=100, null=False)
    penalty1=models.IntegerField(null=False)
    penalty2=models.IntegerField(null=False)
    class Meta:
        db_table = 'matches'

class MatchClub(ModelBase):
    goals = models.IntegerField(null=False, blank=True)
    id_match= models.ForeignKey(
        to="Matches",
        on_delete=models.DO_NOTHING,
        db_column='id_match',
        null=False,
        blank=False,
        related_name='club_matches'
    )
    id_club = models.ForeignKey(
        to="Club",
        on_delete=models.DO_NOTHING,
        db_column='id_club',
        null=False,
        blank=False,
        related_name='club_matches'
    )
    class Meta:
        db_table = 'club_matches'
