from django.contrib import admin
from .models import Book, Movie

# Register my models
admin.site.register(Book)
admin.site.register(Movie)
