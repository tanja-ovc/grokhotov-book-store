from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, viewsets

from books.api.v1.serializers import BookSerializer, CategoriesListSerializer
from books.api.v1.filters import BookFilterSet
from books.models import Book, Category


@method_decorator(name='get', decorator=swagger_auto_schema(
    operation_summary='Получение списка категорий (с подкатегориями)'
))
class CategoriesListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesListSerializer


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_summary='Получение списка книг с возможностью фильтрации '
                      'по разным параметрам'
))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    operation_summary='Получение данных о конкретной книге'
))
class BooksReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookFilterSet
