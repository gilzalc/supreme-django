from rest_framework.routers import DefaultRouter
from myapp.viewsets import BookViewSet

router = DefaultRouter()
router.register('books-api', BookViewSet, basename="books-api")
print(router.urls)
urlpatterns = router.urls
