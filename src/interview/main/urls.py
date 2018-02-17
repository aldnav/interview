from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('get-session/',
         views.GetSessionInfoView.as_view(), name='session-info'),
]
