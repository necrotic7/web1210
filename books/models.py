from django.db import models

class Book(models.Model):
    name = models.CharField('書名',max_length = 20)
    price = models.PositiveIntegerField('價格')
    introduction = models.TextField('介紹')

    def __str__(self):
        return self.name