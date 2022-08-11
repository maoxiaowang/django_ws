from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=64)
    age = models.PositiveIntegerField()


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(max_length=255)
    website = models.CharField(max_length=128, null=True)


class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    author = models.ManyToManyField(Author, related_name='books')
    publisher = models.ForeignKey(Publisher, models.CASCADE, related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
