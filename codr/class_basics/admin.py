from django.contrib import admin

# Register your models here.
from .models import Animal, Publisher, Book, Author

admin.site.register(Animal) 
admin.site.register(Publisher)

admin.site.register(Book)
admin.site.register(Author)