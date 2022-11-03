from django.shortcuts import render, redirect
from .models import BlogItem
from django.views.generic import TemplateView
from django.http.response import HttpResponse
from django.core.exceptions import PermissionDenied

def home_view(request, *args, **kwargs):
	return redirect('blog-list')

def list_view(request, *args, **kwargs):
	ctx = {
	     'blogs': BlogItem.objects.all(),
	     'user': request.user,
	}
	return render(request, 'blog/list.html', context=ctx)



class CreateView(TemplateView):
	
	template_name = 'blog/create.html'

	def get(self,request, *args, **kwargs):
		return render(request, 'blog/create.html', context={})


	def post(self,request, *args, **kwargs):
		    title = request.POST['title']
		    body = request.POST['body']
		    blog_item = BlogItem()
		    blog_item.owner = request.user
		    blog_item.title = title
		    blog_item.body = body
		    blog_item.save()
		    return redirect('blog-list')


class DeleteView(TemplateView):

	template_name = 'blog/delete.html'
	
	def get(self,request, *args, **kwargs):
		if 'id' not in request.GET:
			return HttpResponse('<h1>You\'ve been a naughty boy or girl</h1>', status=400)
		
		try:

			id = int (request.GET['id'])

		except (ValueError,TypeError):

			return HttpResponse('<h1>You are guessing!</h1>', status=400)

		try:
				
			self.blog_item = BlogItem.objects.get(id=id)
		
		except BlogItem.DoesNotExist:
			
			return HttpResponse('<h1>Well that\'s not even there</h1>', status=400)	
		return super().get(request, *args, **kwargs)

	def post(self,  request, *args, **kwargs):	
		if not request.user.is_authenticated:
			raise PermissionDenied('You must be logged in')
		if 'delete' not in request.POST:
			return HttpResponse('<h1>Intruder!</h1>', status=400)

		if request.POST['delete'] != 'YES':
			return HttpResponse('<h1>Intruder!</h1>', status=400)	

		if 'id' not in request.POST:
			return HttpResponse('<h1>Intruder!</h1>', status=400)	

		try:
				
			blog_item = BlogItem.objects.get(id=int(request.POST['id']))
		
		except (ValueError, TypeError, BlogItem.DoesNotExist):
			
			return HttpResponse('<h1>Not found</h1>', status=400)	
		if blog_item.owner != request.user:
			raise PermissionDenied			

		blog_item.delete()
		return redirect('blog-list')	


	def get_context_data(self, *args, **kwargs):
		ctx = super().get_context_data(*args, **kwargs)	
		ctx['blog_item'] = self.blog_item
		print(ctx)
		return ctx





