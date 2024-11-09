from rest_framework import viewsets
from core import models, serializers

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer

class ClubViewSet(viewsets.ModelViewSet):
    queryset = models.Club.objects.all()
    serializer_class = serializers.ClubSerializer

class ChampionshipViewSet(viewsets.ModelViewSet):
    queryset = models.Championship.objects.all()
    serializer_class = serializers.ChampionshipSerializer

class PlayerStatisticsViewSet(viewsets.ModelViewSet):
    queryset = models.PlayerStatistics.objects.all()
    serializer_class = serializers.PlayerStatisticsSerializer

class ClubStatisticsViewSet(viewsets.ModelViewSet):
    queryset = models.ClubStatistics.objects.all()
    serializer_class = serializers.ClubStatisticsSerializer

class MatchesViewSet(viewsets.ModelViewSet):
    queryset = models.Matches.objects.all()
    serializer_class = serializers.MatchesSerializer

class MatchClubViewSet(viewsets.ModelViewSet):
    queryset = models.MatchClub.objects.all()
    serializer_class = serializers.MatchClubSerializer

