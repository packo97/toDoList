from rest_framework.routers import SimpleRouter

from event.views import EventViewSet, EventByAuthorViewSet

router = SimpleRouter()

router.register('', EventViewSet, basename='events')
router.register('by-author', EventByAuthorViewSet, basename='events-by-author')

urlpatterns = router.urls
