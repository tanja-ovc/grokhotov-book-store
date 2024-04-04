import django_filters
from django_filters.rest_framework import filterset

from books.models import Book


class BookFilterSet(filterset.FilterSet):
    category_id = django_filters.NumberFilter(
        field_name='categories', lookup_expr='exact',
        label='Категория (id)'
    )
    category_name = django_filters.CharFilter(
        field_name='categories__title', lookup_expr='icontains',
        label='Категория (название полностью или частично)'
    )
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Книга (название полностью или частично)'
    )
    author = django_filters.CharFilter(
        field_name='authors__name', lookup_expr='icontains',
        label='Автор (имя полностью или частично)'
    )
    status = django_filters.CharFilter(
        lookup_expr='iexact',
        label='Статус (полностью)'
    )
    published_date_later_than = django_filters.DateTimeFilter(
        field_name='publishedDate', lookup_expr='gt',
        label='С даты (формат: ISO)'
    )
    published_date_earlier_than = django_filters.DateTimeFilter(
        field_name='publishedDate', lookup_expr='lt',
        label='По дату (формат: ISO)'
    )

    class Meta:
        model = Book
        fields = (
            'category_id', 'category_name', 'title', 'author', 'status',
            'published_date_later_than', 'published_date_earlier_than'
        )
