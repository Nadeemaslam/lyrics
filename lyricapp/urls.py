from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.articles, name='articles'),
    path('explore/', views.explore, name='explore'),
    path('contact/', views.contact, name='contact'),
    path('results/', views.search_results, name='search'),
    re_path(r'^article/(?P<slug>[\w-]+)/$', views.article, name='article')
]
