from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.views.generic import TemplateView 
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')), 
    path('article/', include('article.urls')),
    path('book/', include('book_vonnegut.urls')),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico')))
]
