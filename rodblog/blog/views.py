from django.shortcuts import render


def home(request):
    template = 'blog/home.html'
    return render(request, template)


def about(request):
    template = 'blog/about.html'
    return render(request, template)