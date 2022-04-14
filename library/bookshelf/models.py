from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class Book(models.Model):
    title = models.CharField(max_length=32)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    issue_date = models.DateField()

    def __str__(self):
        return str(self.author.name)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
