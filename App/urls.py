from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from App import views
urlpatterns = [
    path('', views.index, name='home-page'),
    path('diabetes', views.diabetes, name='intro'),
    path('malariaa', views.malariaa, name='intro'),
    path('pneumonia', views.pneumonia, name='intro'),
    path('predict', views.predict, name='intro'),
    path('upload1',views.upload1,name='intro'),
    path('upload2',views.upload2,name='intro'),
    path('about', views.about, name='intro'),
    path('contact', views.contact, name='intro'),

]
#urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
