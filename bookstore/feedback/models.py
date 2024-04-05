from django.db import models


class Feedback(models.Model):
    name = models.CharField('имя')
    email = models.EmailField('e-mail')
    phone = models.CharField('телефон')
    comment = models.TextField('комментарий')

    class Meta:
        verbose_name = 'фидбэк'
        verbose_name_plural = 'фидбэки'

    def __str__(self):
        return f'фидбэк от {self.name} ({self.email})'
