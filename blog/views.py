from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from django.shortcuts import get_object_or_404
from datetime import datetime

# Create your views here.
def indexPage(request):
    return render(request, 'blog/index.html', {})

def postPage(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'GET':
        return render(request, 'blog/post.html', {'post' : post})
    elif request.method == 'POST':
        body = request.POST.get('body')
        comment = Comment(
            body=body,
            author=UserProfile.objects.last(),
            post = Post.objects.get(slug=slug),
        )
        comment.save()
        return render(request, 'blog/post.html', {'post':post})

def postsPage(request):
    blog_post = Post.objects.all().order_by('-created_at')[:5]
    return render(request, 'blog/posts.html', {'blog_post' : blog_post})