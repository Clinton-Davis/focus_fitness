from django.shortcuts import render
from django.views import generic

# def index(request):
#     """Returns the index page"""
#     return render(request, 'home/index.html')


class HomeView(generic.TemplateView):
    template_name = "index.html"


# def about(request):
#     """Returns the about page"""

#     return render(request, 'home/about.html')


# def contact(request):
#     """Returns the about page"""

#     return render(request, 'home/contact.html')
