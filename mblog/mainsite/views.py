#coding=utf-8
from django.template.loader import get_template
from django.http import HttpResponse,Http404
from django.shortcuts import redirect
from .models import Post,Product
from datetime import datetime
import random
# Create your views here.
def homepage(request):
	template=get_template('index.html')
	now=datetime.now()
	html=template.render(locals())  #把当前内存的局部变量使用字典类型打包
	return HttpResponse(html)

def showpost(request,slug):
	template=get_template('post.html')
	try:
		post=Post.objects.get(slug=slug)
		if post!= None:
			html=template.render(locals())
			return HttpResponse(html)
	except:
		return redirect('/')  #考虑到手动输入错误网址直接返回首页

def about(request): #使用多行文字内容
	template=get_template('about.html')
	html=template.render()
	return HttpResponse(html)

def listing(request): 
	products=Product.objects.all()
	template=get_template('list.html')
	html=template.render({'products':products})
	return HttpResponse(html)

def disp_detail(request,sku):
	try:
		p=Product.objects.get(sku=sku)
	except:
		raise Http404('找不到制定产品编号')
	template=get_template('disp_detail.html')
	html=template.render({'product':p})
	return HttpResponse(html)
