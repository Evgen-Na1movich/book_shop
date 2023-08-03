from django.urls import path

from manager.views import BookView, AddLike

urlpatterns = [
    path('456/', BookView.as_view(), name=''),
    path('add_like/<book_id:int>', AddLike.as_view(), name='add_like')
]
