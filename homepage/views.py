from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import JsonResponse
import json

from .models import VonnegutFact


class HomeView(TemplateView):
    template_name = 'homepage/index.html'


class ProjectView(TemplateView):
    template_name = 'homepage/oproject.html'


def random_fact_api(request):
    '''API для получения случайного факта'''
    random_fact = VonnegutFact.objects.order_by('?').first()
    
    # Инициализация или обновление счетчика в сессии
    viewed_facts = request.session.get('viewed_facts', [])
    total_count = VonnegutFact.objects.count()
    viewed_count = len(viewed_facts)

    # Сбрасываем прогресс, если просмотрели все факты
    if viewed_count >= total_count and total_count > 0:
        viewed_facts = []
        request.session['viewed_facts'] = viewed_facts
        viewed_count = 0

    if random_fact and random_fact.id not in viewed_facts:
        viewed_facts.append(random_fact.id)
        request.session['viewed_facts'] = viewed_facts

    # Проценты
    if total_count > 0:
        progress_percentage = int((viewed_count / total_count) * 100)
    else:
        progress_percentage = 0

    # Пишем все в контекст
    data = {
        'fact_text': random_fact.text if random_fact else 'Факты закончились!',
        'total_facts': total_count,
        'viewed_count': viewed_count,
        'progress_percentage': progress_percentage
    }

    return JsonResponse(data)


def random_fact_view(request):
    '''Основная страница со случайным фактом'''
    random_fact = VonnegutFact.objects.order_by('?').first()
    viewed_facts = request.session.get('viewed_facts', [])

    context = {
        'random_fact': random_fact.text if random_fact else 'Факты закончились!',
        'total_facts': VonnegutFact.objects.count(),
        'viewed_count': len(viewed_facts)
    }
    return render(request, 'homepage/random_fact.html', context)


def custom_404(request, exception):
    return render(request, '404.html', status=404)
