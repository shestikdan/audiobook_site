from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Chapter, ListeningProgress, Book

from django.views.decorators.csrf import csrf_exempt

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
    # Загружаем книгу по первичному ключу с предзагрузкой глав и подглав
    book = get_object_or_404(Book.objects.prefetch_related('chapters__subchapters'), pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

def get_progress(request, chapter_id):
    try:
        progress = ListeningProgress.objects.get(chapter_id=chapter_id)
        return JsonResponse({'last_position': progress.last_position})
    except ListeningProgress.DoesNotExist:
        return JsonResponse({'last_position': 0})

@csrf_exempt
def update_progress(request, chapter_id, seconds):
    if request.method == 'POST':
        chapter = Chapter.objects.get(pk=chapter_id)
        progress, created = ListeningProgress.objects.get_or_create(chapter=chapter)
        if not created:
            progress.total_listened += (seconds - progress.last_position) if seconds > progress.last_position else 0
        progress.last_position = seconds
        progress.save()
        return JsonResponse({'status': 'success'})
    print("Chapter ID:", chapter_id)
    print("Seconds:", seconds)
    return JsonResponse({'status': 'error'}, status=400)
