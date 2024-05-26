from django.test import TestCase, Client
from django.urls import reverse
from library.models import Book, Movie

class BookIntegrationTest(TestCase):

    def test_add_book(self):
        # Arrange : Données du nouveau livre à créer
        new_book_data = {'title': 'Pico Bogue', 'author': 'Dominique Roques'}

        # Act : Envoi d'une requête POST pour créer un nouveau livre
        client = Client()
        response = client.post(reverse('add_book'), data=new_book_data)

        # Assert
        # Redirection vers la page de détail du livre après sa création
        self.assertRedirects(response, reverse('bookInfo', args=[1]), status_code=302, target_status_code=200)
        # Livre créé correctement dans la BD
        book = Book.objects.get(id=1)
        assert book.author == "Dominique Roques"
        assert book.title == "Pico Bogue"

class MovieIntegrationTest(TestCase):

    def test_add_movie(self):
        # Arrange : Données du nouveau film à ajouter
        new_movie_data = {'title': 'The Shawshank Redemption', 'author': 'Frank Darabont', 'length': 142, 'genre': 'Drama'}

        # Act : Envoi d'une requête POST pour créer un nouveau film
        client = Client()
        response = client.post(reverse('add_movie'), data=new_movie_data)

        # Assert
        # Redirection vers la page de détail du film après sa création
        self.assertRedirects(response, reverse('movieInfo', args=[1]), status_code=302, target_status_code=200)
        # Film créé correctement dans la BD
        movie = Movie.objects.get(id=1)
        assert movie.author == "Frank Darabont"
        assert movie.title == "The Shawshank Redemption"
        assert movie.length == 142
        assert movie.genre == "Drama"