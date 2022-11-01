from django.shortcuts import render
from .models import BlogItem

def list_view(request, *args, **kwargs):
	ctx = {
	     'blogs': BlogItem.objects.all(),
	}



	return render(request, 'blog/list.html', context=ctx)



