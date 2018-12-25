
from rest_framework import serializers
from MovieInfo.models import Book,Author,Genre,Subgenre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        exclude=['slug']
        # fields='__all__'
class SubgenreSerializer(serializers.ModelSerializer):

    class Meta:
        model=Subgenre
        # fields='__all__'
        exclude=['slug']
class AuthorSerializer(serializers.ModelSerializer):
    sub_genre=SubgenreSerializer(many=False)
    class Meta:
        model=Author
        fields='__all__'



class BookSerializer(serializers.ModelSerializer):
    author_name=AuthorSerializer(many=False)
    # subgenre=SubgenreSerializer( many=True)
    # genre=GenreSerializer(many=True)
    class Meta:
        model=Book
        fields=['book_name','author_name','status','cost']

    def create(self,validated_data):
        book=Book.objects.create(**validated_data)
        return book


    read_only_fields=['id']

