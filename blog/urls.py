from django.contrib import admin
from django.urls import path

from blog import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:blog_pk>', views.blog_detail, name='blog_detail'),
    path('type/<int:blog_type_pk>', views.blogs_with_type, name='blog_with_type')
]
