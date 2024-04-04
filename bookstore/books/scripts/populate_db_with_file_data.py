# Скрипт запускается командой
# python3 manage.py runscript populate_db_with_file_data

import io
from collections import namedtuple
import requests
import sys

from django.core.files.images import ImageFile
from django.db import transaction

from books.models import Author, Book, Category


file_path = ('https://gitlab.grokhotov.ru/api/v4/projects/197/repository/'
             'files/books.json/raw')


def run():
    sys.stdout.write(
        'Идёт процесс пополнения базы данных...\n'
    )

    response = requests.get(file_path)
    books_json_raw = response.json()

    BookData = namedtuple('BookData', 'book_info authors categories')

    with transaction.atomic():
        books_data = []
        added_books = 0

        for book in books_json_raw:
            if book.get('publishedDate'):
                published = book.pop('publishedDate')
                published_date = published['$date']
                book['publishedDate'] = published_date

            authors = book.pop('authors')
            if '' in authors:
                authors.remove('')

            categories = book.pop('categories')
            if '' in categories:
                categories.remove('')

            if book.get('pageCount') == 0:
                book['pageCount'] = None

            if Book.objects.filter(**book).exists():
                continue

            if book.get('thumbnailUrl'):
                img_response = requests.get(book.get('thumbnailUrl'))
                file_like = io.BytesIO(img_response.content)
                img_file_name = 'default.jpg'
                if book.get('isbn') is not None:
                    img_file_name = book.get('isbn') + '.jpg'
                img_file = ImageFile(file_like, name=img_file_name)
                book['thumbnail'] = img_file

            added_books += 1

            books_data.append(
                BookData(
                    book_info=book, authors=authors, categories=categories
                )
            )

        books_without_relations = [
            Book(**book.book_info) for book in books_data
        ]
        Book.objects.bulk_create(books_without_relations)

        for book in books_data:
            book_without_thumbnail = {
                key: value for key, value in book.book_info.items()
                if key != 'thumbnail'
            }

            created_book = Book.objects.get(**book_without_thumbnail)
            book_authors = []
            for author in book.authors:
                author_obj, created = Author.objects.get_or_create(
                    name=author
                )
                book_authors.append(author_obj)
            created_book.authors.set(book_authors)

            book_categories = []
            if not book.categories:
                new_category_obj, created = Category.objects.get_or_create(
                    title='New'
                )
                book_categories.append(new_category_obj)
            elif book.categories:
                for category in book.categories:
                    category_obj, created = Category.objects.get_or_create(
                        title=category
                    )
                    book_categories.append(category_obj)
            created_book.categories.set(book_categories)

    sys.stdout.write(
        f'База данных пополнена. Получено объектов: {len(books_json_raw)}, '
        f'добавлено объектов: {added_books}.\n'
    )
    if added_books < len(books_json_raw):
        sys.stdout.write(
            'Добавлены не все полученные объекты, т. к. '
            'были найдены и пропущены дубликаты.\n'
        )
