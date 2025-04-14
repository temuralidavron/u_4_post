from django.urls import path

from .views import index,get_post

urlpatterns=[
    path('',index,name='index'),
    path('list/',get_post,name='post-list'),
]