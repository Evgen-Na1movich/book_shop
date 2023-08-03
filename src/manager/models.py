from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    title = models.CharField(max_length=100, verbose_name='название книги')
    test = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    authors = models.ManyToManyField(User, related_name='books')


    def __str__(self):
        return self.title


class Coment(models.Model):
    text = models.TextField()
    data = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    #on_delete=models.CASCADE  при удалении книги будут удаленны все коменты
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

