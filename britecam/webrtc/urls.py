from django.conf.urls import url 
from webrtc import views


urlpatterns = [ 
    url(r'^index$', views.index, name='index'),
    url(r'^home/$',views.home,name='home'),
    url(r'^$',views.main, name='main'),
    url(r'^upload_file/$',views.upload_file, name='upload_file'),
    url(r'^view_archive/$',views.view_archive, name='view_archive'),
    url(r'^delete_filE/(?P<file_id>\S+)/$',views.delete_file, name='delete_file'),
    url(r'^faqs/$',views.faqs,name='faqs'),
    url(r'^feedback/$',views.feedback,name='feedback'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^about/$',views.about,name='about'),
]
