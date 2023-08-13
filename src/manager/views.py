from django.db.models import Count, Prefetch
from django.shortcuts import render, redirect
from django.views import View

from manager.models import Book, Coment


class BookView(View):
    # request содержит все служебные данные, которые приходят с запросом
    def get(self, request):
        comments_for_prefetch = Prefetch('comments',
                                         queryset=Coment.objects.select_related("user").
                                         annotate(likes_comments=Count('likes')))
        # prefeth_related - дополнительно подтягиваем связь
        # annotate каждому объекту запроса добавляет поле
        data = {
            'books': Book.objects.prefetch_related(comments_for_prefetch, 'authors').all()
            # annotate(likes_book=Count('likes'))
        }
        return render(request, "index.html", context=data)


class AddLikeView(View):
    def get(self, request, book_id):
        print(request.user)
        # проверяем зареген ли пользователь и вошел ли он в систему
        if request.user.is_authenticated:
            # через get получаем книгу с определенным book_id
            book = Book.objects.get(id=book_id)
            if request.user in book.likes.all():
                book.likes.remove(request.user)
            else:
                # создастся связь ManyToMany.
                # в add должны передать объект того класса. который указали при создании ManyToMany
                book.likes.add(request.user)
            return redirect('list_view')
