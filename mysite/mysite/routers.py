from rest_framework.routers import DefaultRouter
from myapp.viewsets import BookViewSet

router = DefaultRouter()
router.register('books-abc', BookViewSet, basename="books")
print(router.urls)
urlpatterns = router.urls
