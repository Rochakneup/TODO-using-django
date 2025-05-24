"""
URL configuration for formcrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from os import stat
from django.contrib import admin
from django.urls import include, path
from appcrud.views import index_view, home_view ,login_view , register_view ,todo_view , delete_todo , update_todo
from formcrud import settings
from classform.views import my_view
from school.views import StudentListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('login/', login_view),
    path('register/', register_view),
    path('form', todo_view , name = "form"),
    path('delete/<int:id>/', delete_todo, name='delete_todo'),
    path('update/<int:id>/', update_todo, name='update_todo'),
    path('index/', index_view),
    
    #class based url
    path('cls/',my_view.as_view() , name="class"),
    path('books/',include('classform.urls', namespace = 'classform')),
    path('student/',StudentListView.as_view(), name='student'),

]
