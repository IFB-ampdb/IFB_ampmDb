from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def homeBlog():
	pst = Post.objects.order_by('-published_date')[:2]
	for p in pst:
		p.body = p.body[:100]+' . . . '
	return ('posts', pst)

def blog(request):
	posts = Post.objects.order_by('-published_date')
	return render(request, 'blog/blog.html', {'posts':posts})

def blogPost(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/blogPost.html', {'post':post})
