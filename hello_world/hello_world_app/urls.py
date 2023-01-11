from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('hello_world/', views.hello_world, name='hello_world'),
    path('members/', views.all_members, name='all_members'),
    path('members/<int:id>/', views.member, name='member'),

]
