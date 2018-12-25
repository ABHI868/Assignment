from django.contrib import admin
from MovieInfo.models import Book,Author,Genre,Subgenre
# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Subgenre)