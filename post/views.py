from lib2to3.fixes.fix_input import context

from django.shortcuts import render

from .models import Post

menu=['home','about']


def index(request):
    context={
        'menu':menu
    }
    return render(request,'post/index.html',context)



def get_post(request):
    posts=Post.objects.all()
    context={
        'posts':posts
    }
    return render(request,'post/post_list.html',context)



