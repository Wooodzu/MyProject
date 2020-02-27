from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from wwwap.forms import ContactForm


def home(request):
    return render(request, 'www/home.html')


def about(request):
    return render(request, 'www/about.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            _send_email(email_form=form)
            messages.success(request, f"Email has been sent.")
            return redirect('www-contact')
    form = ContactForm()
    return render(request, 'www/contact.html', {'form': form})


def _send_email(email_form):
    name = email_form.cleaned_data.get('name')
    surname = email_form.cleaned_data.get('surname')
    message = email_form.cleaned_data.get('message')
    email = email_form.cleaned_data.get('email')
    send_mail(
        f'Contact message from website',
        f'Message from {name} {surname}.\n{message}\nE-mail:{email}',
        'django_app@int.pl',
        ['django_app@int.pl'],
        fail_silently=False
    )
