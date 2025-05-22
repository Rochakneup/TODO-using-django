from django.urls import path
from . import views  

app_name = 'classform' 

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  
    path('<slug:slug>/', views.BookDetailView.as_view(), name='book-detail'),  
]
