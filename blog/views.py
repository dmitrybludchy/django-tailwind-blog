from django.shortcuts import render
from .models import Post

def index(request):
    articles = Post.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'blog/index.html', context)


def get_category(request, slug):
    return render(request, 'blog/category.html')
