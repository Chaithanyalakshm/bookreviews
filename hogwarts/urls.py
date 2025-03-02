"""
URL configuration for hogwarts project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Function to redirect root URL to home
def redirect_to_home(request):
    return redirect('home')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_home),  # Redirects '/' to '/home/'
    path('register/', include('books.urls')),
    path('login/', include('books.urls')),
    path('logout/', include('books.urls')),
    path('home/', include('books.urls')),
    path('search/', include('books.urls')),
    path('', redirect_to_home),  # Redirect '/' to '/home/'
    path('', include('books.urls')),  # Includes all routes from books/urls.py

]


