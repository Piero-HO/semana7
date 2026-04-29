from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, GenreViewSet

router = DefaultRouter()

# NUEVO
router.register(r'genres', GenreViewSet)

router.register(r'movies', MovieViewSet)

urlpatterns = router.urls