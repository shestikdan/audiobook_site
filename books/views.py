from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Chapter, ListeningProgress, Book, SubChapter

from django.views.decorators.csrf import csrf_exempt

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

def get_progress(request, subchapter_id):
    try:
        # Получаем прогресс воспроизведения для указанной подглавы
        progress = ListeningProgress.objects.get(subchapter_id=subchapter_id)
        return JsonResponse({'last_position': progress.last_position})
    except ListeningProgress.DoesNotExist:
        # Если прогресса нет, возвращаем 0
        return JsonResponse({'last_position': 0})

@csrf_exempt
def update_progress(request, subchapter_id, seconds):
    if request.method == 'POST':
        try:
            seconds = int(seconds)  # Преобразование в int для безопасности
            subchapter = SubChapter.objects.get(pk=subchapter_id)
            progress, created = ListeningProgress.objects.get_or_create(subchapter=subchapter)
            if not created:
                # Проверяем, что текущее время больше последней записанной позиции
                progress.total_listened += max(0, seconds - progress.last_position)
            progress.last_position = seconds
            progress.save()
            return JsonResponse({'status': 'success'})
        except SubChapter.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'SubChapter not found'}, status=404)
        except ValueError:
            return JsonResponse({'status': 'error', 'message': 'Invalid seconds value'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)