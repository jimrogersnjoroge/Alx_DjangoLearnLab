from django.db import models

# Create your models here.
#Creating my models

#Model Author
class Author(models.Model):
    name = models.CharField(max_length = 50, blank = False, unique = True)


class Book(models.Model):
    title = models.CharField(max_length = 50, blank = False, unique = True)
    publication_year = models.IntegerField(blank = False)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)


