from django.urls import path

from . import views

app_name = 'class_basics'

urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    path('success/', views.SucessView.as_view(), name='success'),
    path('animal/create_animal', views.CreateAnimalFormView.as_view(), name='create_animal'),
    path('animal/', views.AnimalListView.as_view(), name='animal'),
    path('animal/dog', views.DogView.as_view(), name='dog'),
    path('animal/cat', views.CatView.as_view(), name='cat'),
    # ex: /polls/5/

    path('publishers/', views.PublisherListView.as_view(), name="publisher"),
    path('publisher/<int:pk>', views.PublisherView.as_view(), name="detail_publisher"),

]


'''
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), #los detailView deben tener en el path la pk
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    '''