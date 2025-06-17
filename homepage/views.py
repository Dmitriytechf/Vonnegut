from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, View
import random
from .models import VonnegutFact


        
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

