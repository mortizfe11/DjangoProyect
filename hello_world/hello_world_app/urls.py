from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('hello_world/', views.hello_world, name='hello_world'),
    path('members/', views.all_members, name='all_members'),
    #path('members/<int:id>/', views.member, name='member'),
    path('members/create/', views.create_member, name='create_member'),
    path('members/update/', views.update_member, name='update_member'),
    path('members/<slug:slug>/', views.member, name='member'),

]
