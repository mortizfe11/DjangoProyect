from django.urls import path
from . import views

app_name = 'hello_world'

urlpatterns = [
    path('', views.main, name='main'),
    path('hello_world/', views.hello_world, name='hello_world'),
    path('members/', views.all_members, name='all_members'),
    path('members/create/', views.create_member, name='create_member'),
    path('members/update/<slug:slug>', views.update_member, name='update_member'),
    path('members/delete/<slug:slug>', views.delete_member, name='delete_member'),
    path('members/<slug:slug>/', views.member, name='detail_member'),

]
