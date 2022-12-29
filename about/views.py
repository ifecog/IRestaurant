from django.shortcuts import render
from .models import Chef, About

# Create your views here.


def about(request):
    abouts = About.objects.all()
    chefs = Chef.objects.all()
    context = {
        'abouts': abouts,
        'chefs': chefs,
    }

    return render(request, 'pages/about.html', context)
