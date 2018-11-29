from django.shortcuts import render


def subscribed(request):
    return render(request, 'newsletter/subscribed.html')
