from django.urls import path

from . import views

# setting app name 
app_name = 'polls'

# Setting url pattern within polls app
urlpatterns = [
    # index call on polls app || ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # id call in polls  || ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # results on id || ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # Votes on choices || ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]