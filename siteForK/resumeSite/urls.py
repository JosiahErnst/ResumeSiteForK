from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('homePage', views.homePage, name='homePage'),
    path('resumePage', views.resumePage, name='resumePage'),
    path('schedulingPage', views.schedulingPage, name='schedulingPage'),
    path('portfolioPage', views.portfolioPage, name='portfolioPage'),
]