from django.urls import path
from . import views

urlpatterns = [
    path("", views.posts, name='posts'),
    path('posts/<int:id>/', views.post_detail, name='post_details'),
    path('posts/delete/<int:id>/', views.post_delete, name='post_delete')
]
