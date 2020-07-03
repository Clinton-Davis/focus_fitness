from django.shortcuts import render


def index(request):
    """Returns the index page"""

    return render(request, 'home/index.html')


def about(request):
    """Returns the about page"""

    return render(request, 'home/about.html')


def contact(request):
    """Returns the about page"""

    return render(request, 'home/contact.html')
