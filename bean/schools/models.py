# coding=utf-8 
# import os
# import Image

from django.db import models
# from bean.settings import MEDIA_ROOT
# from django.db.models.fields.files import ImageFieldFile

UPLOAD_ROOT = 'uploadImg'

# def make_thumb(path, size = 480):
#     pixbuf = Image.open(path)
#     width, height = pixbuf.size
# 
#     if width > size:
#         delta = width / size
#         height = int(height / delta)
#         pixbuf.thumbnail((size, height), Image.ANTIALIAS)
# 
#         return pixbuf

class Major(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'专业名')
    bio = models.CharField(max_length=300, blank=True, verbose_name=u'简介')
    code = models.CharField(max_length=20, blank=True, verbose_name=u'专业代码')
    
    def __unicode__(self):
        return u'%s' % self.name
    
    class Meta:
        verbose_name = (u'专业')
        verbose_name_plural = (u'专业')

class School(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'学校名称')
    province = models.CharField(max_length=30, blank=True, verbose_name=u'省份')
    city = models.CharField(max_length=30, blank=True, verbose_name=u'城市')
    address = models.CharField(max_length=300, blank=True, verbose_name=u'地址')
    website = models.URLField(blank=True, verbose_name=u'学校网站')
    tel = models.CharField(max_length=30, blank=True, verbose_name=u'联系电话')
    major = models.ManyToManyField(Major, verbose_name=u'专业')
    pic = models.ImageField(upload_to = UPLOAD_ROOT, blank=True, verbose_name=u'学校标志（校徽）')
    date = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return u'%s' % self.name
    
    class Meta:
        verbose_name = (u'学校')
        verbose_name_plural = (u'学校')

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    intro = models.CharField(max_length=300, blank=True, verbose_name=u'摘要')
    content = models.TextField(verbose_name=u'正文')
    author = models.CharField(max_length=30, blank=True, verbose_name=u'作者')
    pic = models.ImageField(upload_to = UPLOAD_ROOT, blank=True, verbose_name=u'资料图片')
    read_times = models.IntegerField(blank=True, verbose_name=u'阅读人数')
    #pic_thumb = models.ImageField(upload_to = THUMB_ROOT, blank = True)
    
    link = models.URLField(blank=True, verbose_name=u'淘宝链接')
    date = models.DateTimeField(auto_now_add = True, verbose_name=u'发表日期')
    sales = models.IntegerField(blank=True, verbose_name=u'销量')
    
    school = models.ForeignKey(School, verbose_name=u'学校')
    major = models.ForeignKey(Major, verbose_name=u'专业')
    
#     def save(self):
#         base, ext = os.path.splitext(os.path.basename(self.image.path))
#         thumb_pixbuf = make_thumb(os.path.join(MEDIA_ROOT, self.image.name))
#         relate_thumb_path = os.path.join(THUMB_ROOT, base + '.thumb' + ext)
#         thumb_path = os.path.join(MEDIA_ROOT, relate_thumb_path)
#         print thumb_path
#         thumb_pixbuf.save(thumb_path)
#         self.pic_thumb = ImageFieldFile(self, self.thumb, relate_thumb_path)
#         super(Article, self).save()
    
    def __unicode__(self):
        return u'%s' % self.title
    
    class Meta:
        verbose_name = (u'文章')
        verbose_name_plural = (u'文章')

# class Content(models.Model):
#     content = models.TextField()
#     image = models.ImageField(upload_to = UPLOAD_ROOT)
#     article = models.ForeignKey(Article)