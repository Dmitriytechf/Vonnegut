from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView

from homepage.views import custom_404

handler404 = custom_404 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')), 
    path('article/', include('article.urls')),
    path('book/', include('book_vonnegut.urls')),
    path('logo.ico', RedirectView.as_view(url=staticfiles_storage.url('logo.ico'))),
]
