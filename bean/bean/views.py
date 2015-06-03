#coding=utf-8

from django.shortcuts import render_to_response
from django.http import  HttpResponse, Http404, HttpResponseRedirect
from schools.models import Major, School, Article

def home(request, name='home'):
    schools = School.objects.all()
    majors = Major.objects.all()
    all_articles = Article.objects.all()
    articles = filter(lambda x : x.pic == '', all_articles)
    produces = filter(lambda x : x.pic != '', all_articles)
    return render_to_response('index.html', {'schools'  :  schools, 
                                             'majors'   :  majors,
                                             'articles' :  articles,
                                             'produces'  :  produces})