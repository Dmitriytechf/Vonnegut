from django.urls import path
from django.views.generic import TemplateView 


urlpatterns = [
    path('', TemplateView.as_view(template_name="list_book/book_kurt.html"), name='book_kurt'),
]