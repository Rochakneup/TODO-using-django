# urls.py
from django.urls import path
from . import views  

app_name = 'classform' 

urlpatterns = [
    # List views
    path('', views.BookListView.as_view(), name='book-list'),  
    path('books/', views.IndexView.as_view(), name='index'),  # Your original view
    
    # CRUD operations
    path('book/create/', views.BookCreateView.as_view(), name='book-create'),
    path('book/<slug:slug>/', views.BookDetailView.as_view(), name='book-detail'),
    path('book/<slug:slug>/edit/', views.BookUpdateView.as_view(), name='book-update'),
    path('book/<slug:slug>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
    
    # Basic view
    path('basic/', views.my_view.as_view(), name='basic-view'),
]
