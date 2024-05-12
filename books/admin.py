from django.contrib import admin
from .models import Book, Chapter, ListeningProgress, SubChapter

admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(SubChapter)
admin.site.register(ListeningProgress)