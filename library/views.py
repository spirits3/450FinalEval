from django.shortcuts import get_object_or_404, render,redirect
from .models import Book, Movie
from django.views import View
from .forms import BookForm, MovieForm

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

class CreateBookView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'create_book.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            new_book = form.save()
            # Rediriger vers la page de détail du livre nouvellement créé
            return redirect('bookInfo', pk=new_book.pk)
        else:
            # Si le formulaire n'est pas valide, réafficher le formulaire avec les erreurs
            return render(request, 'create_book.html', {'form': form})

def movie_info(request, pk):
    """View function for book info."""
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, "movie_info.html", {'movie':movie})

class AddMovieView(View):
    def get(self, request):
        form = MovieForm()
        return render(request, 'add_movie.html', {'form': form})

    def post(self, request):
        form = MovieForm(request.POST)
        if form.is_valid():
            new_movie = form.save()
            # Rediriger vers la page de détail du livre nouvellement créé
            return redirect('movieInfo', pk=new_movie.pk)
        else:
            # Si le formulaire n'est pas valide, réafficher le formulaire avec les erreurs
            return render(request, 'add_movie.html', {'form': form})

class EditMovieView(View):
    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        form = MovieForm(instance=movie)
        return render(request, 'edit_movie.html', {'form': form})

    def post(self, request, pk):
        form = MovieForm(request.POST)
        if form.is_valid():
            print('post')
            edited_movie = form.save()
            # Rediriger vers la page de détail du livre nouvellement créé
            return redirect('movieInfo', pk=edited_movie.pk)
        else:
            # Si le formulaire n'est pas valide, réafficher le formulaire avec les erreurs
            print('bug')
            return render(request, 'edit_movie.html', {'form': form})