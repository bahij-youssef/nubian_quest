from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.core.mail import send_mail


# def contact(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         message = request.POST['message']
#         if request.POST['phone_number']:
#             phone_number = request.POST['phone_number']
#         else:
#             phone_number = ''

#         contact = Contact(first_name=first_name, last_name=last_name,
#                           email=email, message=message, phone_number=phone_number)
#         contact.save()

#         return redirect('submitted')

#     return render(request, 'pages/contact.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'New inquiry from Nubian Quest',
                f"You have a new inquiry from {request.POST['first_name']} {request.POST['last_name']} with the following message: {request.POST['message']}. Contact details: {request.POST['email']}. Please respond at your earliest convenience.",
                'nubianquest01@gmail.com',
                ['info@virtuestudios.co.uk', 'phil.tittensor@hotmail.co.uk']
            )
            return redirect('submitted')
    else:
        form = ContactForm()
        return render(request, 'contacts/contact2.html', {'form': form})


def submitted(request):
    return render(request, 'contacts/contact_submitted.html')
