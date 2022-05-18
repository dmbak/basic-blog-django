from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='blog_index'),
    path('posts/', views.posts, name='all_posts'),
    # path('posts/<slug:slug>', views.post_detail, name='one_post')
    path('posts/<slug:slug>', views.SingePostView.as_view(), name='one_post')
]
