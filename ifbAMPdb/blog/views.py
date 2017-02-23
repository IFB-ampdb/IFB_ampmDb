from django.shortcuts import render, get_object_or_404
from blog.models import Post


#returns a dictionary with a list of the last 2 Blog Posts
def homeBlog():
	pst = Post.objects.order_by('-published_date')[:2]
	return ({'posts': pst})

#loads the blog page with posts ordered by date ( most recent first)
def blog(request):
	posts = Post.objects.order_by('-published_date')
	return render(request, 'blog/blog.html', {'posts':posts})

#renders the Blog Post page
def blogPost(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/blogPost.html', {'post':post})
