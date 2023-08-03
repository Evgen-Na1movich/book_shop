from django.shortcuts import render
from django.views import View

from manager.models import Book


class BookView(View):
    def get(self, request):
        data = {
            'books': Book.objects.all()
        }
        return render(request, "index.html", context=data)

class AddLike(View):
    def get(self, request):
        book = Book.object.get(id=book_id)
        return