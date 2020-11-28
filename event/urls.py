from rest_framework.routers import SimpleRouter

from event.views import EventViewSet

router = SimpleRouter()

router.register('', EventViewSet, basename='events')

urlpatterns = router.urls
