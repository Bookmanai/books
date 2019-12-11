from django.views import generic
from django.shortcuts import get_object_or_404
from .models import Book, Author, Genre
from django.http import HttpResponseRedirect
from .forms import BookpdfForm
from .models import BookPdf
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.urls import path
from django.utils.translation import activate
from django.http import FileResponse, Http404


def upload_file(request):
    if request.method == 'POST':
        form = BookpdfForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = BookpdfForm()
    return render(request, 'upload.html', {'form': form})


class BookListView(generic.ListView):
    model = Book
    paginate_by = 20
    context_object_name = 'book_list'  # your own name for the list as a template variable


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context


class SearchResultsView(ListView):
    model = Book
    template_name = 'search_results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(
            Q(title__icontains=query) | Q(author__first_name__icontains=query) | Q(author__last_name__icontains=query))
        return object_list

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 20
    context_object_name = 'author_list'


class AuthorDetailView(generic.DetailView):
    model = Author

    def author_detail_view(request, primary_key):
        author = get_object_or_404(Author, pk=primary_key)
        return render(request, 'catalog/author_detail.html', context={'author': author})


class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request, primary_key):
        book = get_object_or_404(Book, pk=primary_key)
        return render(request, 'catalog/book_detail.html', context={'book': book})


def index(request):
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()


    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
    }

    return render(request, "index.html", context=context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("../")
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def set_ru(self):
    activate('ru')
    Book.objects.all()
    Author.objects.all()
    return HttpResponseRedirect("../")


def set_en(self):
    activate('en')
    Book.objects.all()
    Author.objects.all()
    return HttpResponseRedirect("../")