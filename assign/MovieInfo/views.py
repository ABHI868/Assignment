from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from MovieInfo.models import Book,Author,Genre,Subgenre
from MovieInfo.serializers import BookSerializer,AuthorSerializer,GenreSerializer,SubgenreSerializer
from rest_framework.permissions import IsAdminUser,IsAuthenticatedOrReadOnly

class BookListInfo(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticatedOrReadOnly,)
    model=Book
    serializer_class=BookSerializer

    def get_queryset(self):
        return Book.objects.all()

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticatedOrReadOnly,)
    serializer_class=BookSerializer
    model=Book
    queryset=Book.objects.all()
    # def get_queryset(self,pk):
    #     return Book.objects.all()

def home(request):
    return render(request,"MovieInfo/base.html")
