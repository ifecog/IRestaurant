from django.shortcuts import render
from .models import Chef

# Create your views here.


def about(request):
    chefs = Chef.objects.all()

    context = {
        'chefs': chefs,
    }

    return render(request, 'pages/about.html')
