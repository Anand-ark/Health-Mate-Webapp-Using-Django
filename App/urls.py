from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from App import views
from django.views.static import serve 
from django.conf.urls import url
urlpatterns = [
    path('', views.index, name='home-page'),
    path('diabetes', views.diabetes, name='intro'),
    path('malariaa', views.malariaa, name='intro'),
    path('covid', views.covid, name='intro'),
    path('predict', views.predict, name='intro'),
    #path('skin', views.skin, name='intro'),
    path('upload1',views.upload1,name='intro'),
    path('upload2',views.upload2,name='intro'),
    path('about', views.about, name='intro'),
    path('contact', views.contact, name='intro'),
    path('hpredict', views.hpredict, name='intro'),
    path('heart', views.heart, name='intro'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
