from django.contrib import admin

from books.models import Author, Book, Category, Subcategory


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'isbn', 'pageCount', 'publishedDate', 'status'
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
