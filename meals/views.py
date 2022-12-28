from django.shortcuts import render
from . models import Feature, Testimonial

# Create your views here.
def home(request):
    features = Feature.objects.all()
    testimonials = Testimonial.objects.all()
    context = {
        'features': features,
        'testimonials': testimonials,
    }
    
    return render(request, 'pages/home.html', context)