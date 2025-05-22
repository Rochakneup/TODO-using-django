from django.utils import timezone
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from classform.models import Books
from django.db.models import F



#class based view 
class my_view(View):
    def get(self, request):
        return  HttpResponse("<h1> Class based view base class </h1>")
    

class IndexView(TemplateView):
    template_name = 'books.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['books'] = Books.objects.all()
        return context
    

class BookDetailView(DetailView):

    model = Books
    template_name = 'book-detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        post = Books.objects.filter(slug=self.kwargs.get('slug'))
        post.update(count=F('count') + 1)

        context['time'] = timezone.now()

        return context