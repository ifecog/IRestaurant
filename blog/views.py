from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator

# Create your views here.


def posts(request):
    posts = Post.objects.all().order_by('-upload_time')
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': page_obj,
    }
    return render(request, 'blog/posts.html', context)


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {
        'post': post,
    }

    return render(request, 'blog/post_detail.html', context)
