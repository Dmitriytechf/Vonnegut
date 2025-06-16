from django.urls import path, include
from .views import HomeView, ProjectView, random_fact_view, FaviconView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('random-fact/', random_fact_view, name='random_fact'),
    path('oproject/', ProjectView.as_view(), name='oproject'),
    path('favicon.ico', FaviconView.as_view()),
]