"""desitomato URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,patterns,include
from django.contrib import admin

from english.views import show_article_list,open_article,response,performance_stats,login,register,register2,load_more,update2,sample_test,review,tutorial,generate_question,verb_forms_gen,findvocab,bookmarks,testing,lookup,aboutus,index,logout,impwords,hehe,start,delbookmark
urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^homepage/$', show_article_list,name='show_article_list_view'),
    url(r'^article/(?P<articleid>[0-9]{1,})/$', open_article,name='article_url'),
    url(r'^responseapi/$',response),
    url(r'^performance/$',performance_stats),
    url(r'^login/$',login,name='login_view'),
    url(r'^register/$',register,name='register_view'),
    url(r'^register2/$',register2,name='register_view2'),
    url(r'^loadmore/(?P<id>[0-9]{1,})/$',load_more),
    url(r'^update2/$',update2),
    url(r'^ass/$',sample_test),
    url(r'^review/$',review),
    url(r'^tutorial/(?P<headname>[a-z]{1,})/$', tutorial,name='tutorial'),
    url(r'^gen/$',generate_question),
    url(r'^yoyo/$',verb_forms_gen),
    url(r'^findvocab/$',findvocab),
    url(r'^bookmark/$',bookmarks),
    url(r'^testing/$',testing),
    url(r'^lookup/$',lookup),
    url(r'^about/$',aboutus),
    url(r'^logout/$',logout,name='logout_view'),
    url(r'^$',index),
    url(r'^do/$',impwords),
    url(r'^privacy/$',hehe),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^start/$',start),
    url(r'^deletebookmark/$',delbookmark),)