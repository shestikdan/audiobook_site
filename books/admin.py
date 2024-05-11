from django.contrib import admin
from .models import Book, Chapter, ListeningProgress

admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(ListeningProgress)