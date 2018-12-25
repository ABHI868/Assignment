from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from djmoney.models.fields import MoneyField
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Book(models.Model):
    book_name=models.CharField(max_length=100)
    author_name=models.OneToOneField('Author', on_delete=models.CASCADE)
    option=(('p',"published"), ('u',"unpublished"))
    status=models.CharField(choices=option, default="p", max_length=2)
    cost = MoneyField(max_digits=5, decimal_places=2, default_currency='INR')
    publish_date_time=models.DateTimeField(auto_now=False)

    def __str__(self):
        return str(self.book_name)
    
class Author(models.Model):
    author_name=models.CharField(max_length=100)
    author_rating=models.FloatField(validators=[MinValueValidator(0.0),
                                       MaxValueValidator(9.9)] )
    sub_genre=models.OneToOneField('Subgenre' ,on_delete=models.CASCADE)
    about=models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.author_name)

class Genre(models.Model):
    genre_name=models.CharField(max_length=80 , unique=False)
    genre_details=models.CharField(max_length=100)
    slug=models.SlugField(unique=False)

    class Meta:
        ordering=['genre_name']
    def __str__(self):
        return str(self.genre_name)

def pre_save_genre(sender, instance ,*args, **kwargs):
    slug=slugify(instance.genre_name)
    flag=Genre.objects.filter(slug=slug).exists()
    if flag:
        # slug="{}-{}".format(slug,str(instance.id))
        slug="%s-%s" %(slug,instance.id)
    else:
        instance.slug=slug
pre_save.connect(pre_save_genre,sender=Genre)


class Subgenre(models.Model):
    genre_name=models.OneToOneField('Genre',on_delete=models.CASCADE,unique=False)
    subgenre_name=models.CharField(max_length=100, null=True)
    description=models.TextField(null=True, blank=True)
    slug=models.SlugField(unique=False)

    def __str__(self):
        return str(self.subgenre_name)


def pre_save_subgenre(sender, instance ,*args, **kwargs):
    slug=slugify(instance.subgenre_name)
    flag=Subgenre.objects.filter(slug=slug).exists()
    if flag:
        # slug="{}-{}".format(slug,str(instance.id))
        slug="%s-%s" %(slug,instance.id)
    else:
        instance.slug=slug
pre_save.connect(pre_save_subgenre,sender=Subgenre)


