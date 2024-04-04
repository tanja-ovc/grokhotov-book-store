from django.urls import include, path
from rest_framework.routers import DefaultRouter

from books.api.v1.views import BooksReadOnlyViewSet, CategoriesListAPIView

router_v1 = DefaultRouter()


router_v1.register(r'', BooksReadOnlyViewSet)


urlpatterns = [
    path('categories/', CategoriesListAPIView.as_view()),
    path('', include(router_v1.urls)),
]
