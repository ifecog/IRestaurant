from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator
from .forms import CommentForm
from django.urls import reverse


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
    recents = Post.objects.all().order_by('upload_time')[:6]
    comments = Comment.objects.filter(post=post)
    comments_count = Comment.objects.all().filter(post=post).count()
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()

            return redirect(reverse('post_detail', kwargs={'id': id}))
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'recents': recents,
        'comments': comments,
        'comment_form': comment_form,
        'count': comments_count,
    }

    return render(request, 'blog/post_detail.html', context)
