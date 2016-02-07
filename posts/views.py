from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404

from .models import Post
from .form import PostForm


def home(request):
	return render(request,"index.html",{})

def post(request):
	queryset_list = Post.objects.all()

	paginator = Paginator(queryset_list, 4) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
	    queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)

	context = {
		'posts': queryset,
	}
	return render(request,"post/index.html",context)

def postshow(request, id):
	queryset = Post.objects.get(id=id)
	context = {
		'post': queryset,
	}  
	return render(request,"post/show.html",context)

def postcreate(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Not Successfully Created")
		return HttpResponseRedirect('/posts/')
	else:
		messages.error(request, "Successfully Created")
	context = {
		"form": form,
	}
	return render(request,"post/new.html",context)

def postupdate(request, id):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Item Saved", extra_tags='some-tag')
		return HttpResponseRedirect('/posts/'+id)

	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}
	return render(request,"post/new.html",context)
def postdestroy(request, id):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = Post.objects.get(id=id)
	instance.delete()
	messages.success(request, "Successfully deleted", extra_tags='delete-post')
	return redirect('/posts/')


