from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, viewsets

from books.api.v1.serializers import (
    BooksSerializer, CategoriesSerializer, SingleBookSerializer
)
from books.api.v1.filters import BookFilterSet
from books.models import Book, Category


@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_summary='Получение списка категорий (с подкатегориями)'
))
class CategoriesListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_summary='Получение списка книг с возможностью фильтрации '
                      'по разным параметрам'
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_summary='Получение данных о конкретной книге'
))
class BooksReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.prefetch_related('authors', 'categories')
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookFilterSet

    def get_serializer_class(self):
        if self.action == 'list':
            return BooksSerializer
        elif self.action == 'retrieve':
            return SingleBookSerializer

