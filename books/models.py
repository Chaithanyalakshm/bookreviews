from django.db import models
from django.db.models import Avg

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

    def average_rating(self):
        avg_rating = self.reviews.aggregate(Avg('rating'))['rating__avg']
        return round(avg_rating, 1) if avg_rating else 0  # Default to 0 if no reviews

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    comment = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"Review for {self.book.title}"
