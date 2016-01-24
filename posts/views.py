from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .form import PostForm


def home(request):
	return render(request,"index.html",{})

def post(request):
	queryset = Post.objects.all()
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
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect('/posts/')
	context = {
		"form": form,
	}
	return render(request,"post/new.html",context)

def postupdate(request, id):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect('/posts/'+id)

	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}
	return render(request,"post/new.html",context)