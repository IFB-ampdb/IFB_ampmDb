from django.shortcuts import render
from .models import Post

# Create your views here.

def homeBlog():
    pst = Post.objects.order_by('published_date')[:3]
    return {'posts': pst}
