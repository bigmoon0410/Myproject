#coding=utf-8

from django.contrib import admin
from .models import Post,NewTable,Product
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display=('title','slug','pub_date')  #让文章在显示的时候除了title以外，还可以加上张贴的日期和时间等内容

admin.site.register(Post,PostAdmin)
admin.site.register(NewTable)
admin.site.register(Product)

