# coding=utf-8 

from django.shortcuts import render_to_response
from django.http import  HttpResponse, Http404, HttpResponseRedirect
from schools.models import Major, School, Article

def _get_content(content_dict={}):
    schools = School.objects.all()
    majors = Major.objects.all()
    content_dict['schools'] = schools
    content_dict['majors'] = majors
    return content_dict

def home(request, name='home'):
    all_articles = Article.objects.all()
    articles = filter(lambda x : x.pic == '', all_articles)
    produces = filter(lambda x : x.pic != '', all_articles)
    return render_to_response('index.html', _get_content({'articles' :  articles,
                                                          'produces'  :  produces}))
    
def show_school(request, name = 'school'):
    error = False
    if 'sid' in request.GET:
        sid = request.GET['sid']
        if not sid:
            error = True
        else:
            q_school = School.objects.filter(id=sid)
            if not q_school :
                error = True
            else:
                q_school = q_school[0]
                print q_school.major.all()
                q_major  = ''
                articles = Article.objects.filter(school=q_school)
                if 'mid' in request.GET:
                    mid = request.GET['mid']
                    if mid:
                        q_major = Major.objects.filter(id=mid)
                        if not q_major:
                            articles = Article.objects.filter(school=q_school, major=q_major)  
                return render_to_response('display_items.html',
                                          _get_content({'q_school'      : q_school, 
                                                        'q_major'       : q_major,
                                                        'articles'      : articles,
                                                        'error'         : error}))
    return render_to_response('404.html', _get_content({'error' : error,}))




