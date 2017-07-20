# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.urls import reverse

# Create your views here.
def post_list(request):
	posts = Post.objects.all().order_by('published_date')
	return render(request,'blog/post_list.html', {'posts':posts})

def post_detail(request,pk):
	#posts = Post.objects.get(pk=pk)	
	posts = get_object_or_404(Post,pk=pk)
	return render(request,'blog/post_detail.html', {'posts':posts})

def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.autor = request.user
			post.published_date = timezone.now()
			post.save()
			pk=post.pk
			return redirect(reverse('blog:postdetail',args=[pk]))
	else:
		form = PostForm()
	#form = PostForm()
	#posts = get_object_or_404(Post,pk=pk)
	return render(request,'blog/post_edit.html', {'form':form})

def post_edit(request,pk):
	post = get_object_or_404(Post,pk=pk)
	if request.method == 'POST':
		form = PostForm(request.POST,instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.autor = request.user
			#post.published_date = timezone.now()
			post.save()
			pk=post.pk
			return redirect(reverse('blog:postdetail',args=[pk]))
	else:
		form = PostForm(instance=post)
		#form = PostForm()
		#posts = get_object_or_404(Post,pk=pk)
	return render(request,'blog/post_edit.html', {'form':form})

