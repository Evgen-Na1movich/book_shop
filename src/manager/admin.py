from django.contrib import admin

from manager.models import Book, Coment


class ComentInline(admin.StackedInline):
    model = Coment
    extra = 1


class BookAdmin(admin.ModelAdmin):
    inlines = [ComentInline]


admin.site.register(Book, BookAdmin)
admin.site.register(Coment)