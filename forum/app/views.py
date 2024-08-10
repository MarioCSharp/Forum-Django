from django.shortcuts import render, get_object_or_404
from .models import Post

def homepage(request):
    return render(request, 'home.html')

def posts(request):
    allPosts = Post.objects.all()
    return render(request, 'posts.html', {'posts': allPosts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post_details.html', {'post': post})