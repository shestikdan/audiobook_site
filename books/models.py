from django.db import models
from django.core.validators import MinValueValidator

class Book(models.Model):
    name = models.CharField(max_length=100)  # Увеличенная длина для имени книги
    author = models.CharField(max_length=100)  # Увеличенная длина для имени автора
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)  # Путь для сохранения изображений обложек


class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='chapters')
    name = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='chapters/')
    duration = models.IntegerField(default=0, editable=False)
    

class ListeningProgress(models.Model):
    chapter = models.ForeignKey('Chapter', on_delete=models.CASCADE, related_name='progress')
    last_position = models.IntegerField(default=0)  # время в секундах, где пользователь остановился
    total_listened = models.IntegerField(default=0)  # суммарное время прослушивания для поддержки функционала быстрого перемотки

    def __str__(self):
        return f'{self.chapter.book.name} - {self.chapter.name} : {self.last_position}s'