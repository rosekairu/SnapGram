from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'SnapGram'

urlpatterns = [
    path('', views.index, name = "index"),
    path('myprofile/', views.myprofile, name="myprofile"),
    path('update-profile/',views.update_profile,name = 'update-profile'),
    path('updateprofilephoto/',views.update_profile_photo,name = 'update-profile-photo'),
    path('create/post', views.create_post, name="newpost"),
    path('search', views.search_profile, name="search"),
    path('image/<int:image_id>', views.view_image, name="image"),
    path('image/like/<int:image_id>', views.like_image, name="like"),
    path('image/comment/<int:image_id>', views.comment_image, name="comment"),
    path('image/update/<int:image_id>',views.update_caption, name = 'update_caption'),
    path('image/delete/<int:image_id>',views.delete_image, name = 'delete-image'),
    path('profile/<str:username>', views.user_profile, name="profile"),
    path('accounts/logout', views.logout_user, name="logout"),
    path('profile/follow/<int:user_id>', views.follow_user, name="follow")
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


