from rest_framework.routers import SimpleRouter

from event.views import EventViewSet, EventByAuthorViewSet

router = SimpleRouter()

#router.register('', EventViewSet, basename='events')
router.register('', EventByAuthorViewSet, basename='events-by-author') #-list e -detail

urlpatterns = router.urls
