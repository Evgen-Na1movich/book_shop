from django.contrib.auth.models import User
from django.core.management import BaseCommand

from manager.models import Book


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        Book.objects.all().delete()
        # user1 = User.objects.create(username="Boris", password='useruser')
        # user2 = User.objects.create(username="Tony", password='useruser')
        # user3 = User.objects.create(username="Lena", password='useruser')
        # User.objects.bulk_create([user1, user2, user3])
        users = User.objects.all()

        book1 = Book(title='book1', text='text for book1')
        book2 = Book(title='book1', text='text for book1')
        book3 = Book(title='book1', text='text for book1')
        Book.objects.bulk_create([book1, book2, book3])

        for book in Book.objects.all():
            book.authors.add(users[0], users[2])
            book.save()
