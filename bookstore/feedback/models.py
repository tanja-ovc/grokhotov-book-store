from django.db import models


class Feedback(models.Model):
    name = models.CharField('имя')
    email = models.EmailField('e-mail')
    phone = models.CharField('телефон')
    comment = models.TextField('комментарий')
