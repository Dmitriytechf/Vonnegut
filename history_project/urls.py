from django.contrib import admin
from django.urls import include, path
from homepage.views import FaviconView
from django.conf import settings
from django.views.generic import TemplateView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')), 
    path('article/', include('article.urls')),
    path('book/', include('book_vonnegut.urls')),
]
