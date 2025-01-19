"""
URL configuration for BookCRUD project.

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
from django.urls import path
from store.views import BookCreateView, BookListView, BookDetailView, BookDeleteView,BookUpdateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/add/',BookCreateView.as_view(),name='book_add'),
    path('books/all/',BookListView.as_view(),name='book_list'),
    path('books/<int:pk>/',BookDetailView.as_view(),name='book_detail'),
    path('books/<int:pk>/remove/',BookDeleteView.as_view(),name='book_delete'),
    path('books/<int:pk>/change/',BookUpdateView.as_view(),name='book-edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
