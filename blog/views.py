from django.shortcuts import render, redirect
from .models import BlogItem

def home_view(request, *args, **kwargs):
	return redirect('blog-list')

def list_view(request, *args, **kwargs):
	ctx = {
	     'blogs': BlogItem.objects.all(),
	}
	return render(request, 'blog/list.html', context=ctx)



