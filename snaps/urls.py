from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .import views
# from django.urls import path, re_path


urlpatterns=[
    url(r'^$', views.timeline, name='allTimelines'),
    url(r'^profile/', views.find_profile, name='find_profile'),
    url(r'^image/(\d+)', views.single_image, name='singleImage'),
    url(r'^user/(\d+)', views.user_profile, name='userProfile'),
    url(r'^single_image/likes/(\d+)', views.single_image_like, name="singleImageLike"),
    url(r'^profile/', views.find_profile, name="findProfile"),
    url(r'^new/comment/(?P<username>[-_\w.]+)/$', views.new_comment, name="newComment"),
    url(r'^new/status/(?P<username>[-_\w.]+)/$', views.new_status, name="new_status"),
    url(r'^accounts/profile/', views.profile, name="myProfile"),        

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)