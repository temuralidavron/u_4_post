from django.shortcuts import render
menu=['home','about','post']


def index(request):
    context={
        'menu':menu
    }
    return render(request,'post/index.html',context)



