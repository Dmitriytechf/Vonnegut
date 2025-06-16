from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, View
import random
from .models import VonnegutFact
from django.contrib.staticfiles import finders


class FaviconView(View):
    def get(self, request, *args, **kwargs):
        favicon_path = finders.find('img/favicon.ico')
        if favicon_path:
            with open(favicon_path, 'rb') as f:
                return HttpResponse(f.read(), content_type='image/x-icon')
        return HttpResponse(status=404)
        
class HomeView(TemplateView):
    template_name = 'homepage/index.html'

class ProjectView(TemplateView):
    template_name = 'homepage/oproject.html'

def random_fact_view(request):
    all_facts = VonnegutFact.objects.all()
    facts_list = list(all_facts)
    
    random_fact = random.choice(facts_list)
    context = {
        'random_fact': random_fact.text,
        'total_facts': len(facts_list)
    }
    
    return render(request, 'homepage/random_fact.html', context)

