from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator

from .models import Group, Post, User
from posts.forms import PostForm


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context) 


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:settings.ITEMS_COUNT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)

def profile(request, username):
    posts = Post.objects.filter(author__username=username)
    user = User.objects.get(username=username)
    post_count = posts.count()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'post_count': post_count,
        'user': user
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    posts = Post.objects.filter(author__id=post.author_id)
    post_count = posts.count()
    context = {
        'post': post,
        'post_count': post_count,
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get(username=request.user.username)
            post.save()
            return redirect('/profile/' + request.user.username)

    form = PostForm(request.GET)
    posts_group = Group.objects.all()
    context = {
        'posts_group': posts_group,
        'form': form,
    }
    return render(request, 'posts/create_post.html', context)


def post_edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    if post.author_id != request.user.id:
        return redirect('/posts/' + str(post_id))
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get(username=request.user.username)
            post.save()
            return

    form = PostForm(request.GET)
    posts_group = Group.objects.all()
    context = {
        'posts_group': posts_group,
        'form': form,
        'is_edit': True,
        'text': post.text,
    }
    return render(request, 'posts/create_post.html', context)
