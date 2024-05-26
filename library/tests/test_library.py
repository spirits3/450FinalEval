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
    def setUp(self):
        Movie.objects.create(title='The lord of the rings: The fellowship of the ring', author='J. R. Tolkien', length=178, genre='Fantasy')
        Movie.objects.create(title='Harry Potter and the goblet of fire', author='J. K. Rowling', length=157, genre='Fantasy')
        Movie.objects.create(title='Fight Club', author='David Fincher', length=139, genre='Thriller psychologic')

    def test_add_movie(self):
        # Arrange : Données du nouveau film à ajouter
        new_movie_data = {'title': 'The Shawshank Redemption', 'author': 'Frank Darabont', 'length': 142, 'genre': 'Drama'}

        # Act : Envoi d'une requête POST pour créer un nouveau film
        client = Client()
        response = client.post(reverse('add_movie'), data=new_movie_data)

        # Assert
        # Redirection vers la page de détail du film après sa création
        self.assertRedirects(response, reverse('movieInfo', args=[4]), status_code=302, target_status_code=200)
        # Film créé correctement dans la BD
        movie = Movie.objects.get(id=4)
        assert movie.author == "Frank Darabont"
        assert movie.title == "The Shawshank Redemption"
        assert movie.length == 142
        assert movie.genre == "Drama"

    def test_edit_movie(self):
        # Arrange : Données du film à éditer        
        edit_movie = Movie.objects.get(title="Fight Club")
        edit_movie_data = {'title': edit_movie.title, 'author': edit_movie.author, 'length': 132, 'genre': edit_movie.genre}

        # Act : Envoi d'une requête POST pour éditer un nouveau film
        client = Client()
        response = client.post(reverse('edit_movie', args=[1]), data=edit_movie_data)
        print(response)

        # Assert
        # Redirection vers la page de détail du film après son édition
        self.assertRedirects(response, reverse('movieInfo', args=[1]), status_code=302, target_status_code=200)
        # Film créé correctement dans la BD
        movie = Movie.objects.get(id=1)
        assert movie.author == "David Fincher"
        assert movie.title == "Fight Club"
        assert movie.length == 132
        assert movie.genre == "Thriller psychologic"

    def test_movie_are_correctly_added(self):
        # test seulement si les films ont correctement été ajouté via la fixture dans la BD
        lordOfTheRings = Movie.objects.get(title="The lord of the rings: The fellowship of the ring")
        harryPotter = Movie.objects.get(title="Harry Potter and the goblet of fire")
        assert lordOfTheRings.author == 'J. R. Tolkien'
        assert lordOfTheRings.length==178
        assert lordOfTheRings.genre == 'Fantasy'

        assert harryPotter.author == 'J. K. Rowling'
        assert harryPotter.length == 157
        assert harryPotter.genre == 'Fantasy'