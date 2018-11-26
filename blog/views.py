from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post


def blog(request):
    posts = Post.objects.order_by('-date_published').filter(is_draft=False)

    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        'posts': paged_posts,
    }

    return render(request, 'blog/blog_posts.html', context)


def single_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post,
    }

    return render(request, 'blog/single_post2.html', context)
