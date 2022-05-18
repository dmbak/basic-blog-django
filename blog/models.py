import email
from django.db import models
from django.core.validators import MinLengthValidator
from sqlalchemy import null

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=50)
    image = models.ImageField(upload_to="posts", null=True)
    slug = models.SlugField(unique=True, db_index=True)
    date = models.DateField(auto_now=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, null=True, on_delete=models.SET_NULL, related_name="posts")
    tags = models.ManyToManyField(Tag)


class Comment(models.Model):
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField()
    text = models.TextField(max_length=1000)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
