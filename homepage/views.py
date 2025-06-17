from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, View
import random
from .models import VonnegutFact


        
class HomeView(TemplateView):
    template_name = 'homepage/index.html'


class ProjectView(TemplateView):
    template_name = 'homepage/oproject.html'


def random_fact_view(request):
    '''Случайные факты про Воннегута'''
    random_fact = VonnegutFact.objects.order_by('?').first()
    
    # Инициализация или обновление счетчика в сессии
    viewed_facts = request.session.get('viewed_facts', [])
    
    if random_fact and random_fact.id not in viewed_facts:
        viewed_facts.append(random_fact.id)
        request.session['viewed_facts'] = viewed_facts
        
    context = {
        'random_fact': random_fact.text,
        'total_facts': VonnegutFact.objects.count(),
        'viewed_count': len(viewed_facts)
    }
    
    return render(request, 'homepage/random_fact.html', context)

