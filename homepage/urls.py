from django.urls import include, path

from .views import HomeView, ProjectView, random_fact_view, random_fact_api

urlpatterns = [
    # Главная
    path('', HomeView.as_view(), name='home'),
    # Случайный факт
    path('random-fact/', random_fact_view, name='random_fact'),
    path('api/random-fact/', random_fact_api, name='random_fact_api'),
    # О проекте
    path('oproject/', ProjectView.as_view(), name='oproject'),
]