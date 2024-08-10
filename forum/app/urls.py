from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("posts/", views.posts, name='posts'),
    path('posts/<int:id>/', views.post_detail, name='post_details')
]
