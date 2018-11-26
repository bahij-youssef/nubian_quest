from django.shortcuts import render, redirect
from .models import Contact


def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        message = request.POST['message']
        if request.POST['phone_number']:
            phone_number = request.POST['phone_number']
        else:
            phone_number = ''

        contact = Contact(first_name=first_name, last_name=last_name,
                          email=email, message=message, phone_number=phone_number)
        contact.save()

        return redirect('submitted')

    return render(request, 'pages/contact.html')


def submitted(request):
    return render(request, 'pages/contact_submitted.html')
