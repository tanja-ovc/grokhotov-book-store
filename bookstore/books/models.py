from django.db import models


class Category(models.Model):
    title = models.CharField('название категории', unique=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    title = models.CharField('название подкатегории', unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories',
        verbose_name='название категории'
    )

    class Meta:
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField('имя автора', unique=True)

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField('название книги')
    isbn = models.CharField('ISBN')
    pageCount = models.SmallIntegerField(
        'кол-во страниц', blank=True, null=True
    )
    publishedDate = models.DateTimeField(
        'дата публикации', blank=True, null=True
    )
    thumbnailUrl = models.URLField(
        'ссылка на картинку', blank=True, null=True
    )
    thumbnail = models.ImageField('картинка', upload_to='books_images/')
    shortDescription = models.TextField(
        'краткое описание', blank=True, null=True
    )
    longDescription = models.TextField(
        'подробное описание', blank=True, null=True
    )
    status = models.CharField('статус')
    authors = models.ManyToManyField(
        Author, related_name='books', verbose_name='авторы'
    )
    categories = models.ManyToManyField(
        Category, related_name='books', verbose_name='категории'
    )

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    def __str__(self):
        return self.title
