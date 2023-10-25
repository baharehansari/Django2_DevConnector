from django.db import models
from accounts.models import *
from django.utils.text import slugify
from django.urls import reverse, reverse_lazy
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(UserProfile, related_name='post_like', null=True, blank=True)
    dislike = models.ManyToManyField(UserProfile, related_name='post_dislike', null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save()
        if not self.slug:
            self.slug = slugify(self.title)
            self.save()

    def get_absolute_url(self):
        return reverse_lazy("post", kwargs={'slug':self.slug})

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True)
    is_validate = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.body}, date:{self.created_at}, post:{self.post.title}'