from django.shortcuts import get_object_or_404, render
from .models import Book, Movie

def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_movies = Movie.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits+1

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_visits': num_visits, 'num_movies': num_movies},
    )

def book_info(request, pk):
    """View function for book info."""
    book = get_object_or_404(Book, pk=pk)
    return render(request, "book_info.html", {'book':book})

def movie_info(request, pk):
    """View function for book info."""
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, "movie_info.html", {'movie':movie})