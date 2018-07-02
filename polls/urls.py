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
    path('submit_survey_compact/<int:user_id>/<str:survey_string>', views.submit_survey_compact, name='submit_survey_compact'),
    path('get_surveys_yesterday/', views.get_surveys_yesterday, name='get_surveys_yesterday'),
    path('get_checkins_yesterday/', views.get_checkins_yesterday, name='get_checkins_yesterday'),
    path('clear_data_before_yesterday', views.clear_data_before_yesterday, name='clear_data_before_yesterday'),
    path('submit_feedback/<int:user_id>/<int:week>/<str:avg_weight>/<str:avg_steps>/<int:total_active_min>/<str:height>/', views.submit_feedback, name='submit_feedback'),
    path('get_feedback/<int:user_id>/', views.get_feedback, name='get_feedback'),
    path('remove_feedback/<int:user_id>/', views.remove_feedback, name='remove_feedback')
]
