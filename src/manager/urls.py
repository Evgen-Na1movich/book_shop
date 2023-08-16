from django.urls import path

from manager.views import BookView, AddLikeView, InfoBook

urlpatterns = [
    path('', BookView.as_view(), name='list_view'),
    path('add_like/<int:book_id>', AddLikeView.as_view(), name='add_like'),
    path('info_book/<int:book_id>', InfoBook.as_view(), name='info_book'),
]
