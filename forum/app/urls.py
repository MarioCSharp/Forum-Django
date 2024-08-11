from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.posts, name='posts'),
    path('posts/<int:id>/', views.post_detail, name='post_details'),
    path('posts/delete/<int:id>/', views.post_delete, name='post_delete'),
    path('posts/add/', views.post_add, name='post_add'),
    path('posts/edit/<int:id>', views.post_edit, name='post_edit')
]
