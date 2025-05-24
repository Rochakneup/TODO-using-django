from django.utils import timezone
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from classform.models import Books
from django.db.models import F
from django import forms


# Form for Create and Update operations
class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'slug', 'genre', 'author', 'isbn']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
        }


#  class-based view 
class my_view(View):
    def get(self, request):
        return HttpResponse("<h1> Class based view base class </h1>")


# ListView 
class BookListView(ListView):
    model = Books
    template_name = 'book_list.html'
    context_object_name = 'books'
    paginate_by = 10  
    ordering = ['-id']  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_books'] = Books.objects.count()
        context['current_time'] = timezone.now()
        return context


class IndexView(TemplateView):
    template_name = 'books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Books.objects.all()
        return context


# DetailView 
class BookDetailView(DetailView):
    model = Books
    template_name = 'book-detail.html'
    context_object_name = 'book'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
      
        Books.objects.filter(slug=self.kwargs.get('slug')).update(count=F('count') + 1)
        
        context['time'] = timezone.now()
        return context


# CreateView 
class BookCreateView(CreateView):
    model = Books
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('classform:book-list')

    def form_valid(self, form):
        messages.success(self.request, 'Book created successfully!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Add New Book'
        context['button_text'] = 'Create Book'
        return context


# UpdateView 
class BookUpdateView(UpdateView):
    model = Books
    form_class = BookForm
    template_name = 'book_form.html'
    context_object_name = 'book'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_success_url(self):
        return reverse('classform:book-detail', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        messages.success(self.request, 'Book updated successfully!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = f'Edit: {self.object.title}'
        context['button_text'] = 'Update Book'
        return context


# DeleteView 
class BookDeleteView(DeleteView):
    model = Books
    template_name = 'book-delete.html'
    context_object_name = 'book'
    success_url = reverse_lazy('classform:book-list')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Book deleted successfully!')
        return super().delete(request, *args, **kwargs)