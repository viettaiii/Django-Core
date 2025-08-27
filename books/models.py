from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    genre = models.CharField(max_length=50, choices=[('fiction', 'Fiction'), ('non-fiction', 'Non-Fiction'), ('sci-fi', 'Sci-Fi')])
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title