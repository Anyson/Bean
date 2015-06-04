from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from schools.models import Major, School, Article
from django.template.loader import render_to_string

@dajaxice_register
def get_articles(request, sid = None, mid = None, page=0):
    print 'sid:', sid,'; mid:', mid
    dajax = Dajax()
    if not sid or not mid :
        return dajax.json()
    school_list = School.objects.filter(id=sid)
    major_list = Major.objects.filter(id=mid)
    if not school_list:
        return dajax.json()
    if not major_list and page != 0:
        return dajax.json()
    q_school = school_list[0]
    articles = []
    if page == 0:
        articles = Article.objects.filter(school=q_school)
    else :
        q_major = major_list[0]
        articles = Article.objects.filter(school=q_school, major=q_major)
    render = render_to_string('list_article_intro.html', { 'articles': articles })
    dajax.assign('#show_articles', 'innerHTML', render)
    return dajax.json()