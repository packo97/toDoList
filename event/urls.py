from django.urls import path
from rest_framework.routers import SimpleRouter

from event.views import EventByAuthorViewSet, AuthorView

router = SimpleRouter()

#router.register('', EventViewSet, basename='events')
router.register('', EventByAuthorViewSet, basename='events-by-author') #-list e -detail

urlpatterns = router.urls
urlpatterns.append(path('author/<str:username>',AuthorView.as_view()))
