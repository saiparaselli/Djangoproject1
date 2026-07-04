from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add_video,name='add_video'),
    path('videos/',views.view_videos,name='view_videos'),
    path('play/<int:id>/',views.play_video,name='play_video'),
    path(
    'update/<int:id>/',
    views.update_video,
    name='update_video'
),

path(
    'delete/<int:id>/',
    views.delete_video,
    name='delete_video'
),
]