from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .decorators import isOwner

def blogs(request):
    posts = models.Blog.objects.all()
    # for post in posts:
    #     post.img = models.BlogImg.objects.filter(blog__id = post.id).last().img
    context = {
        'posts':posts
    }
    return render(request, 'blogs.html', context)


def blog_detail(request, id):
    blog = models.Blog.objects.get(id=id)
    # comment_count = models.Comment.objects.filter(blog=blog).count()
    comments = models.Comment.objects.filter(blog=blog)
    context = {
        'blog':blog,
        # 'comment_count':comment_count,
        'comment_count':comments.count(),
        'comments':comments
    }
    return render(request, 'blog-detail.html', context)


def comment_create(request):
    message = request.POST['message']
    blog_id = request.POST['blog_id']
    models.Comment.objects.create(
        author=request.user,
        body=message,
        blog_id=blog_id
    )
    return redirect('blog_detail', blog_id)
 
    
@isOwner
def comment_edit(request, comment_id):
    comment = get_object_or_404(models.Comment, id=comment_id)

    if request.method == 'POST':
        message = request.POST['message']
        comment.body = message
        comment.save()
        return redirect('blog_detail', id=comment.blog.id)
    
    context = {
        'comment': comment
    }
    return render(request, 'comment_edit.html', context)

