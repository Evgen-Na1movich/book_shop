from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db.models import Count

from manager.models import Book


class Command(BaseCommand):
    """"
    Эта команда преднозначена для передачи кол-ва лайков, которые уже поставили, в новую переменную.
    И будет приплюсовывать новые лайки.
    """

    def handle(self, *args, **options):
        books = Book.objects.annotate(likes_book=Count('likes'))
        for kniga in books:
            # передаем все лайки в филд count_likes с анатированной таблицы annotate(likes_book=Count('likes'))
            kniga.count_likes = kniga.likes_book
        Book.objects.bulk_update(books, ['count_likes'], batch_size=1000)
