from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from irestaurant import settings


# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['name']

            try:
                subject = [subject]
                message = [message]
                from_email = email
                recipient_list = [settings.EMAIL_HOST_USER]
                send_mail(subject, message, from_email,
                          recipient_list, fail_silently=False)

                form.save()

                messages.success(
                    request, 'Your inquiry has been submitted. We will get back to you shortly')
                return redirect('contact')

            except BadHeaderError:
                return HttpResponse('Bad Response')

    else:
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'pages/contact.html', context)
