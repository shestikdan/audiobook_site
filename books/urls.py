from django.urls import path
from .views import book_list, book_detail, update_progress, get_progress

urlpatterns = [
    path('', book_list, name='book_list'),
    path('book/<int:pk>/', book_detail, name='book_detail'),
    path('update-progress/<int:chapter_id>/<int:seconds>/', update_progress, name='update_progress'),
    path('get-progress/<int:chapter_id>/', get_progress, name='get_progress'),
    
]