from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.contenttypes.models import ContentType

from .models import Post
from comments.models import Comment
from .form import PostForm

def home(request):
	return render(request,"index.html",{})

def post(request):
	queryset_list = Post.objects.all()

	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(Q(title__icontains=query)|Q(content__icontains=query)|Q(user__username__icontains=query)).distinct()
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
	if not request.user.is_authenticated():
		raise Http404
	instance = get_object_or_404(Post, id=id)
	queryset = Post.objects.get(id=id)
	content_type = ContentType.objects.get_for_model(Post)
	obj_id = instance.id
	comments = Comment.objects.filter(content_type=content_type,object_id=obj_id)
	#comments = Comment.objects.filter(user=request.user)
	#comments = Comment.objects.filter(post=instance)
	context = {
		'post': queryset,
		'comments':comments
	}  
	return render(request,"post/show.html",context)

def postcreate(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404

	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
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


