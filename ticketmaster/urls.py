from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="tickemtaster"),
    path('view_favorites/', views.view_favorites, name='view_favorites'),
    path('create_favorite/', views.create_favorite, name='create_favorite'),
    path('delete_favorite/', views.delete_favorite, name='delete_favorite'),
    path('update_favorite_attending/', views.update_favorite_attending, name='update_favorite_attending'),
]
