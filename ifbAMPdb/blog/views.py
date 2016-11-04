from django.shortcuts import render, get_object_or_404
from .models import Post
from django.db.models import Q


# Create your views here.

def homeBlog():
	pst = Post.objects.order_by('published_date')[:3]
	return ('posts', pst)

def blog(request):
	posts = Post.objects.order_by('published_date')
	return render(request, 'blog/blog.html', {'posts':posts})

def blogPost(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/blogPost.html', {'post':post})

class ampBasicSearch():
	def get_queryset(self):
        result = super(BlogSearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(content__icontains=q) for q in query_list))
            )

        return result
