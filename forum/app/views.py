from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def homepage(request):
    return render(request, 'home.html')

def posts(request):
    allPosts = Post.objects.all()
    return render(request, 'posts.html', {'posts': allPosts})
    

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post_details.html', {'post': post})

def post_delete(request, id):
    post = Post.objects.get(pk=id)
    post.delete()

    return redirect('/')

def post_add(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'post_add.html', {'form': form})
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            saved_form = form.save()

            return redirect(f'/posts/{saved_form.id}/')
        
        return render(request, 'post_add.html', {'form': form})
    
def post_edit(request, id):
    if request.method == 'GET':
        post = Post.objects.get(pk=id)
        form = PostForm(instance=post)

        return render(request, 'post_edit.html', {'form': form})
    elif request.method == 'POST':
        post = Post.objects.get(pk=id)
        edited = PostForm(request.POST, instance=post)
        if edited.is_valid():
            saved = edited.save()
            return redirect(f'/posts/{saved.id}/')
        
        return render(request, 'post_edit.html', {'form': edited})