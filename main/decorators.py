from functools import wraps
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Comment

def isOwner(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        comment_id = kwargs['comment_id']
        comment = get_object_or_404(Comment, id=comment_id)
        if comment.author == request.user:
            return view_func(request, *args, **kwargs)
        else:
            messages.error("Siz bu 'comment' yaratuvchisi emasiz!")
    return wrapper
    
    
    
