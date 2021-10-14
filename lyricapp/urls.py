from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.articles, name='articles'),
    path('explore/', views.explore, name='explore'),
    path('contact/', views.contact, name='contact'),
    path('results/', views.search_results, name='search'),
    path('article/(?P<slug>[\w-]+)/$', views.article, name='article')
]
