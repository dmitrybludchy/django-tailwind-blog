from django.shortcuts import render
from .models import Post, Category, Tag
from django.views.generic import ListView, DetailView


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 6


def index(request):
    articles = Post.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'blog/index.html', context)


def get_category(request, slug):
    return render(request, 'blog/category.html')
