from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>', views.blogDetail, name='blogDetail'),
    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact, name='contact'),
]