from django.urls import path
from . import views

from .views import (
    main_page,
    hello_world_page,
    all_members_page,
    detail_member_page,
    create_member_page,
    update_member_page,
    delete_member_page,
)

app_name = 'hello_world'

urlpatterns = [
    path('', main_page, name='main'),
    path('hello_world/', hello_world_page, name='hello_world'),
    path('members/', all_members_page, name='all_members'),
    path('members/create/', create_member_page, name='create_member'),
    path('members/update/<slug:slug>', update_member_page, name='update_member'),
    path('members/delete/<slug:slug>', delete_member_page, name='delete_member'),
    path('members/<slug:slug>/', detail_member_page, name='detail_member'),

]
