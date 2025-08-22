from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="article/article.html"), name='article'),  
    path('slaughterhouse/', TemplateView.as_view(template_name="article/article1.html"), name='article1'),
    path('catcradle/', TemplateView.as_view(template_name="article/article2.html"), name='article2'),
    path('breakfast/', TemplateView.as_view(template_name="article/article3.html"), name='article3'),
]
