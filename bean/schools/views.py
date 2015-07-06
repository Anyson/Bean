# coding=utf-8 

from django.shortcuts import render_to_response
#from django.http import  HttpResponse, Http404, HttpResponseRedirect
from schools.models import Major, School, Article

def _get_content(content_dict={}):
    schools = School.objects.all()
    majors = Major.objects.all()
    content_dict['schools'] = schools
    content_dict['majors'] = majors
    return content_dict

def home(request, name='home'):
    all_articles = Article.objects.all().order_by('read_times')
    articles = filter(lambda x : x.pic == '', all_articles)
    produces = filter(lambda x : x.pic != '', all_articles)
    if len(articles) > 8:
        articles = articles[len(articles)-8:len(articles)]
    if len(produces) > 5:
        produces = produces[len(produces)-5:len(produces)]
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
                articles = Article.objects.filter(school=q_school).order_by("date").reverse()
                if 'mid' in request.GET:
                    mid = request.GET['mid']
                    if mid:
                        q_major = Major.objects.filter(id=mid)
                        if q_major:
                            q_major = q_major[0]
                            articles = Article.objects.filter(school=q_school, major=q_major)
                        else :
                            q_major= ''
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
                q_article.read_times += 1
                q_article.save()
                #q_article.content = html.format_html(q_article.content)
                recommend_pro = Article.objects.exclude(id=aid).filter(school=q_article.school, major=q_article.major).order_by("sales").reverse()
                recommend_pro = filter(lambda x : x.pic != '', recommend_pro)
                if len(recommend_pro) > 5:
                    recommend_pro = recommend_pro[len(recommend_pro)-5:len(recommend_pro)]
                return render_to_response('display_detail_item.html',
                                          _get_content({'article'       : q_article,
                                                        'recommend_pro' : recommend_pro,
                                                        'error'         : error}))
                
    return render_to_response('404.html', _get_content({'error' : error,}))

def show_search_result(request, name="search"):
    error = False
    if 'q' in request.GET:
        q_search = request.GET['q']
        if not q_search:
            error = True
        else:
            articles = Article.objects.filter(title__icontains=q_search).order_by('date').reverse()
            counter = len(articles)
            page_list = []
            if counter :
                total_page = (counter / 10) if (counter % 10 == 0) else (counter / 10 + 1)
                articles = articles[0:10]
                page_list = range(1, total_page + 1)
            return render_to_response('search.html',
                                          _get_content({'q_search'      : q_search,
                                                        'articles'      : articles,
                                                        'total_counter' : counter,
                                                        'current_page'  : 1 , 
                                                        'page_list'     : page_list,
                                                        'error'         : error}))
            
    return render_to_response('404.html', _get_content({'error' : error,}))



def page_not_found(request):
    return render_to_response('404.html', _get_content())

def page_error(request):
    return render_to_response('500.html', _get_content())
