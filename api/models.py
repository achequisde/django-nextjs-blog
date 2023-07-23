from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)

    title = models.CharField(max_length=100)

    content = models.TextField()

    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    @property
    def extract(self):
        return self.content[:250]

    def __str__(self):
        return self.title
