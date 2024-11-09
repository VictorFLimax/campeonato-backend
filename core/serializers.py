from rest_framework import serializers
from core import models

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Player
        fields = '__all__'

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Club
        fields = '__all__'

class ChampionshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Championship
        fields = '__all__'

class PlayerStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlayerStatistics
        fields = '__all__'

class ClubStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClubStatistics
        fields = '__all__'

class MatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Matches
        fields = '__all__'
class MatchClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MatchClub
        fields = '__all__'