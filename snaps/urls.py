from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$', views.home, name='home'),
    url(r'^search', views.search_results, name='search_results'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^new/image$', views.new_image, name='new-image'),
    url(r'^follow/(\d+)',views.follow,name="follow"),
    url(r'^edit/profile$', views.update_profile, name='update_profile'),
    url(r'^comment/(\d+)/$', views.comment, name='comment'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^likes/(?P<id>\d+)',views.likes,name ='like')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)