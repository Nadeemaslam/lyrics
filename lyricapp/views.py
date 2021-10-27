from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Articles
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    recentposts = Articles.objects.filter(status=1).order_by('-created_on')[:4]
    context = {'articles': recentposts}
    return render(request, 'lyricapp/index.html', context)

def articles(request):
    articles = Articles.objects.filter(status=1).order_by('-created_on')[:10]
    context = {'articles': articles}
    return render(request, 'lyricapp/articles.html', context)


def article(request, slug):
    try:
        article = Articles.objects.get(slug=slug)
        context = {'article': article}
        return render(request, 'lyricapp/article.html', context)
    except ObjectDoesNotExist:
        return render(request, template_name='lyricapp/article.html')

from django.db.models import Q


def search_results(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        articles = Articles.objects.filter(Q(title__contains=searched) | Q(content__contains=searched))
        discover = Articles.objects.filter(status=1).order_by('-created_on')[:4]
        context = {'articles': articles,
                   'discover': discover
                   }
        return render(request, 'lyricapp/searchresults.html', context)
    else:
        return render(request, 'lyricapp/searchresults.html')


def explore(request):
    recentposts = Articles.objects.filter(status=1).order_by('-created_on')
    page = request.GET.get('page', 1)

    ltpos = Articles.objects.filter(status=1).order_by('-created_on')[:4]
    paginator = Paginator(recentposts, 4)
    try:
        recentposts = paginator.page(page)
    except PageNotAnInteger:
        recentposts = paginator.page(1)
    except EmptyPage:
        recentposts = paginator.page(paginator.num_pages)
    context = {'articles': recentposts,
               'ltpos': ltpos}

    return render(request, 'lyricapp/explore.html', context)


def contact(request):
    return render(request, template_name='lyricapp/contact.html')
