from django.contrib import admin
from .models import VonnegutFact

@admin.register(VonnegutFact)
class VonnegutFactAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at')
    search_fields = ('text', )
