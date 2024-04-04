from rest_framework import serializers

from books.models import Author, Book, Category, Subcategory


class SubcategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = ('id', 'title')


class CategoriesListSerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'subcategories')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title')


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('id', 'name')


class RelatedBookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)
    categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = (
            'id', 'title', 'thumbnail', 'authors', 'categories'
        )


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    related_books = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = (
            'id', 'title', 'isbn', 'pageCount', 'publishedDate',
            'thumbnail', 'shortDescription', 'longDescription', 'status',
            'authors', 'categories', 'related_books'
        )

    def get_related_books(self, obj):
        retrieved_book_categories = obj.categories.all()
        related_books = Book.objects.filter(
            categories__in=retrieved_book_categories
        ).exclude(id=obj.id)[:5]
        serializer = RelatedBookSerializer(related_books, many=True)
        return serializer.data
