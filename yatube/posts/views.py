from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect

from django.core.paginator import Paginator

from .models import Post, Group, Contact, User

from ..users.forms import CreatePost, ContactForm

from ..users.views import PostForm

POST_COUNT = 10


def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, POST_COUNT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'text': 'Это главная страница проекта Yatube',
        'posts': posts,
        'page_obj': page_obj
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    """Здесь будет информация о группах проекта Yatube."""
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POST_COUNT]
    context = {
        'text': 'Здесь будет информация о группах проекта Yatube',
        'group': group,
        'posts': posts
    }
    return render(request, 'posts/group_list.html', context)


def user_contact(request):
    contact = Contact.objects.get(pk=3)
    form = ContactForm(instance=contact)
    return render(request, 'users/contact.html', {'form': form})


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = author.posts.all()
    paginator = Paginator(posts, POST_COUNT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    title = f'Все посты пользователя {username}'
    post_count = author.posts.count()
    context = {
        'title': title,
        'page_obj': page_obj,
        'page_number': page_number,
        'post_count': post_count

    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    posts = get_object_or_404(Post, pk=post_id)
    author = posts.author
    pub_date = posts.pub_date
    post_count = author.posts.count()
    context = {
        'posts': posts,
        'author': author,
        'pub_date': pub_date,
        'post_count': post_count
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    if request.method == 'POST':
        form = CreatePost(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('posts:profile', request.user)
    form = CreatePost()
    return render(request, 'posts/posts_create.html', {'form': form})


@login_required
def post_edit(request, post_id):
    posts = get_object_or_404(Post, id=post_id)

    if request.method == 'GET':
        if not posts.author == request.user:
            return redirect('posts:post_detail', post_id)
        form = PostForm(instance=posts)
        context = {
            'form': form,
            'posts': posts
        }
        return render(request, 'posts/posts_create.html', context)

    form = PostForm(request.POST or None, instance=posts)
    if form.is_valid():
        form.save()
    return redirect('posts:post_detail', post_id)
