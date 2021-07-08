from django.urls import path
from . import views

urlpatterns = [
    path('books', views.books),
    path('books/create', views.create_book),
    path('books/<int:id>', views.one_book),
    path('books/<int:id>/delete', views.delete_book),
    path('books/add_author', views.add_author),
    path('authors', views.authors),
    path('authors/create', views.create_author),
    path('authors/<int:id>', views.one_author),
    path('authors/<int:id>/delete', views.delete_author),
    path('authors/add_book', views.add_book)
]