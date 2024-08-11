from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def homepage(request):
    return render(request, 'home.html')

def posts(request):
    if request.method == 'GET':
        allPosts = Post.objects.all()
        form = PostForm()
        return render(request, 'posts.html', {'posts': allPosts, 'form': form})
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            return redirect(f'/posts/{new_post.id}/')

        allPosts = Post.objects.all()
        return render(request, 'posts.html', {'posts': allPosts, 'form': form})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post_details.html', {'post': post})

def post_delete(request, id):
    post = Post.objects.get(pk=id)
    post.delete()

    return redirect('/posts')