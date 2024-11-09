from rest_framework.routers import DefaultRouter
from core import viewsets

router = DefaultRouter()
router.register('player', viewsets.PlayerViewSet)
router.register('club', viewsets.ClubViewSet)
router.register('championship', viewsets.ChampionshipViewSet)
router.register('playerstatistics', viewsets.PlayerStatisticsViewSet)
router.register('clubstatistics', viewsets.ClubStatisticsViewSet)
router.register('matches', viewsets.MatchesViewSet)
router.register('matchclub', viewsets.MatchClubViewSet)

urlpatterns = router.urls