from django.shortcuts import render, redirect


def index_view(request, *args, **kwargs):
	return render(request, 'home/index.html', context={})

