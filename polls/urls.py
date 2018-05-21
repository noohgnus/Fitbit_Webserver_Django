from django.urls import path, re_path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:pk>/', views.UserView.as_view(), name='user'),
    path('ping/<int:user_id>/', views.ping, name='ping'),
    path('checkin/<int:user_id>/<int:ping_type>/', views.checkin, name='checkin'),
    path('submit_survey/<int:user_id>/<str:survey_string>', views.submit_survey, name='submit_survey'),
    path('get_survey/<int:user_id>/', views.get_survey, name='get_survey')
]
