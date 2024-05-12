from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)

class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='chapters')
    name = models.CharField(max_length=200)

class SubChapter(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='subchapters')
    name = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='subchapters/')
    #duration = models.DurationField(default=0, editable=False)  # используем DurationField для хранения времени

'''class ListeningProgress(models.Model):
    subchapter = models.ForeignKey(SubChapter, on_delete=models.CASCADE, related_name='progress')
    last_position = models.DurationField(default=0)  # время в секундах, где пользователь остановился, используем DurationField
    total_listened = models.DurationField(default=0)  # суммарное время прослушивания

    def __str__(self):
        return f'{self.subchapter.chapter.book.name} - {self.subchapter.chapter.name} - {self.subchapter.name}: {self.last_position}s'''

class ListeningProgress(models.Model):
    subchapter = models.ForeignKey(SubChapter, on_delete=models.CASCADE, related_name='progress')
    last_position = models.IntegerField(default=0)  # время в секундах
    total_listened = models.IntegerField(default=0)  # суммарное время прослушивания