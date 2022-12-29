from django.shortcuts import render
from .models import Menu, Booking
from .forms import BookingForm

# Create your views here.


def menu_list(request):
    menus = Menu.objects.all()
    context = {
        'menus': menus
    }

    return render(request, 'pages/menu.html', context)


def booking(request):
    booking_form = BookingForm()

    if request.method == 'POST':
        booking_form = BookingForm(request.POST)

        if booking_form.is_valid():
            booking_form.save()

    context = {
        'booking_form': booking_form,
    }

    return render(request, 'pages/booking.html', context)
