#coding=utf-8
from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from schools.models import Major, School, Article
from django.template.loader import render_to_string

@dajaxice_register
def get_articles(request, sid = None, mid = None, page=0):
    print 'sid:', sid, '; mid:', mid, '; page:', page 
    dajax = Dajax()
    if not sid or not mid :
        return dajax.json()
    try :
        sid = int(sid)
        mid = int(mid)
        page = int(page)
    except Exception:
        dajax.alert(u'请求参数有误')
        return dajax.json()
    school_list = School.objects.filter(id=sid)
    if not school_list:
        return dajax.json()
    
    q_school = school_list[0]
    articles = []
    
    if mid == -1:
        articles = Article.objects.filter(school=q_school)
    else:
        major_list = Major.objects.filter(id=mid)
        if not major_list :
            return dajax.json()
        q_major = major_list[0]
        articles = Article.objects.filter(school=q_school, major=q_major)
    counter = len(articles)
    page_list = []
    if counter :
        total_page = (counter / 10) if (counter % 10 == 0) else (counter / 10 + 1)
        if page >= total_page:
            return dajax.json()
        elif page < 0:
            page = 0
        start = page * 10
        end = start + 10
        if end > counter:
            end = counter
        articles = articles[start:end]
        
        page_list = range(1, total_page + 1)
    
    render = render_to_string('list_article_intro.html', { 'articles'     : articles, 
                                                           'current_page' : page + 1, 
                                                           'page_list'    : page_list})
    dajax.assign('#show_articles', 'innerHTML', render)
    dajax.assign('#q_major', 'value', mid)
    return dajax.json()