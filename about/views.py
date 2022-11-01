from django.shortcuts import render
# from django.http.response import HttpResponse

# Create your views here.

def home(request, *args, **kwargs):
	# return HttpResponse('<h1>Hi and Welcome!</h1>')
	return render(request, 'about/home.html', context={})

def contact(request, *args, **kwargs):
	# return HttpResponse('<h1>Hi and Welcome!</h1>')
	return render(request, 'about/contact.html', context={})
