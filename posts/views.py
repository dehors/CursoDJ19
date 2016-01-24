from django.shortcuts import render

from django.http import HttpResponse
from .models import Post

# Create your views here.
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