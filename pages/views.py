from django.shortcuts import render
import cloudinary
cloudinary.config(
    cloud_name='virtuestudios',
    api_key='717278387128216',
    api_secret='tW4gJ6LCcX-8AISG2_wDPZQscnw'
)


def index(request):

    context = {
        'book': cloudinary.CloudinaryImage('nubian_quest/book.png').build_url(secure=True, quality=60),
        'image3': cloudinary.CloudinaryImage('nubian_quest/image3.jpg').build_url(secure=True, quality=60, height=800, crop='fit', fetch_format='auto'),
        'image1_original': cloudinary.CloudinaryImage('nubian_quest/image1_original.jpg').build_url(secure=True, quality=60, height=800, crop='fit', fetch_format='auto'),
        'image2_original': cloudinary.CloudinaryImage('nubian_quest/image2_original.jpg').build_url(secure=True, quality=60, height=800, crop='fit', fetch_format='auto'),
        'image7': cloudinary.CloudinaryImage('nubian_quest/image7.jpg').build_url(secure=True, quality=60, height=800, crop='fit', fetch_format='auto'),
        'image4': cloudinary.CloudinaryImage('nubian_quest/image4.jpg').build_url(secure=True, quality=60, height=800, crop='fit', fetch_format='auto'),
        'image5': cloudinary.CloudinaryImage('nubian_quest/image5.jpg').build_url(secure=True, quality=60, height=800, crop='fit', fetch_format='auto'),
        'image8': cloudinary.CloudinaryImage('nubian_quest/image8.jpg').build_url(secure=True, quality=60, height=800, crop='fit', fetch_format='auto'),
    }

    return render(request, 'pages/index.html', context)


def about(request):

    context = {
        'book': cloudinary.CloudinaryImage('nubian_quest/book.png').build_url(secure=True, quality=40),
        'author': cloudinary.CloudinaryImage('nubian_quest/author.jpg').build_url(secure=True, quality=40),
    }

    return render(request, 'pages/about.html', context)


def shop(request):

    return render(request, 'pages/shop.html')
