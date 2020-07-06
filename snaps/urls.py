from django.urls import path

from . import views

app_name = 'SnapGram'

urlpatterns = [
    path('', views.index, name = "index"),
    path('myprofile/', views.myprofile, name="myprofile"),
    path('create/post', views.create_post, name="newpost"),
    path('search', views.search, name="search"),
    path('image/<int:image_id>', views.view_image, name="image"),
    path('image/like/<int:image_id>', views.like_image, name="like"),
    path('image/comment/<int:image_id>', views.comment_image, name="comment"),
    path('profile/<str:username>', views.user_profile, name="profile"),
    path('accounts/logout', views.logout_user, name="logout"),
    path('profile/follow/<int:user_id>', views.follow_user, name="follow")
]
