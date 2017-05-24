from django.conf.urls import url
from myfirsttime import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^game', views.GameView.as_view()),
    url(r'^about', views.AboutView.as_view()),
    url(r'^highscores', views.ScoresView.as_view()),
    url(r'^scores', views.ScoreAPIView.as_view())
]   

urlpatterns = format_suffix_patterns(urlpatterns)