from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from django.views import generic

#--- TemplateView
class HomeView(TemplateView):

    template_name = 'index.html'

def step1(request):
    context = {'title':'step1. 연구 목표 설정'}
    return render(request, 'step1.html', context=context)

def step2(request):
    context = {'title':'step2. 데이터 획득'}
    return render(request, 'step2.html', context=context)

def step3(request):
    context = {'title':'step3. 데이터 준비'}
    return render(request, 'step3.html', context=context)

def step4(request):
    context = {'title':'step4. 데이터 탐색'}
    return render(request, 'step4.html', context=context)

def step5(request):
    context = {'title':'step5. 데이터 모델링'}
    return render(request, 'step5.html', context=context)

def step6(request):
    context = {'title':'step6. 발표'}
    return render(request, 'step6.html', context=context)
