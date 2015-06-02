# coding=utf-8 
from django.contrib import admin
from schools.models import Major, School, Article

# class ContentAdmin(admin.StackedInline):
#     model = Content
#     admin.site.register(Content)
# 
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('title', 'date', 'author')
#     radio_fields = {'post_status': admin.VERTICAL,
#                     'type': admin.VERTICAL,
#                     'comment_status': admin.VERTICAL}
#     inlines = [ContentAdmin,]

class MajorAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'bio')
    
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'tel')
    filter_horizontal = ('major',)
    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'intro', 'school', 'major')
    

admin.site.register(Major, MajorAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Article, ArticleAdmin)
