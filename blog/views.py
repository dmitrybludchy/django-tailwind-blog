from django.shortcuts import render

def index(request):
    text = "Hello world"
    context = {
        'context_text': text,
    }
    return render(request, 'blog/index.html', context)
