from django.urls import path
from . import views

app_name = 'hello_world'

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('hello_world/', views.HelloWorldView.as_view(), name='hello_world'),
    path('members/', views.AllMembersView.as_view(), name='all_members'),
    path('members/create/', views.create_member, name='create_member'),
    path('members/update/<slug:slug>', views.update_member, name='update_member'),
    path('members/delete/<slug:slug>', views.delete_member, name='delete_member'),
    path('members/<slug:slug>/', views.MemberView.as_view(), name='detail_member'),
    path('members/success/', views.MemberView.as_view(), name='success'),

]
