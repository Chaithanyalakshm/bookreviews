from django.urls import path
from .views import register, login_view, logout_view, home, search_books, book_detail

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home, name='home'),
    path('search/', search_books, name='search_books'),
    path('book/<int:book_id>/', book_detail, name='book_detail'),
]
