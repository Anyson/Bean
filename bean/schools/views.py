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
                q_major  = ''
                articles = Article.objects.filter(school=q_school)
                counter = len(articles)
                page_list = []
                if counter :
                    total_page = (counter / 10) if (counter % 10 == 0) else (counter / 10 + 1)
                    articles = articles[0:10]
                    page_list = range(1, total_page + 1)
                return render_to_response('display_items.html',
                                          _get_content({'q_school'      : q_school, 
                                                        'q_major'       : q_major,
                                                        'articles'      : articles,
                                                        'current_page'  : 1 , 
                                                        'page_list'     : page_list,
                                                        'error'         : error}))
    return render_to_response('404.html', _get_content({'error' : error,}))


def show_article(request, name="article"):
    error = False
    if 'aid' in request.GET:
        aid = request.GET['aid']
        if not aid:
            error = True
        else:
            q_article = Article.objects.filter(id=aid)
            if not q_article :
                error = True
            else:
                q_article = q_article[0]
                return render_to_response('display_detail_item.html',
                                          _get_content({'article'       : q_article,
                                                        'error'         : error}))
                
    return render_to_response('404.html', _get_content({'error' : error,}))

