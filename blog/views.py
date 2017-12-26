# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.
def index(request):
	articles=models.Article.objects.all()
	return render(request,'blog/index.html',{'articles':articles})
	#return render(request,'blog/index.html')

def article_page(request,article_id):
	article=models.Article.objects.get(pk=article_id)
	return render(request,'blog/article_page.html',{'article':article})