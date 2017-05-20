from django.conf.urls import url
from myfirsttime import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^scores', views.ScoreView.as_view())
]   

urlpatterns = format_suffix_patterns(urlpatterns)