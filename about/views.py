from django.shortcuts import render, redirect



def contact(request, *args, **kwargs):
	return render(request, 'about/contact.html', context={})

