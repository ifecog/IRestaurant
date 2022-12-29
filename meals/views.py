from django.shortcuts import render
from . models import Feature, Testimonial
from menu.models import Category

# Create your views here.
def home(request):
    features = Feature.objects.all()
    testimonials = Testimonial.objects.all()
    categories = Category.objects.all()
    context = {
        'features': features,
        'testimonials': testimonials,
        'categories': categories,
    }
    
    return render(request, 'pages/home.html', context)