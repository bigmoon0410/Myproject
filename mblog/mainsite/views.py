#coding=utf-8
from django.template.loader import get_template
from django.http import HttpResponse
from .models import Post
from datetime import datetime
# Create your views here.
def homepage(request):
	template=get_template('index.html')
	posts=Post.objects.all()
	now=datetime.now()
	html=template.render(locals())  #把当前内存的局部变量使用字典类型打包
	return HttpResponse(html)