from django.urls import path

from hotel import views

urlpatterns = [
    path('', views.index, name='index'),
    path('room/res/<int:id>', views.room_res, name='room_res'),
    path('user/profile/', views.profile, name='profile'),
    path('delete-res/<int:pk>', views.delete_res, name='delete_res'),
    path('edit/', views.edit, name='edit'),
    path('add-room/', views.add_room, name='add_room'),
    path('edit-room/<int:pk>', views.edit_room, name='edit_room'),
    path('delete-room/<int:pk>', views.delete_room, name='delete_room')
]

