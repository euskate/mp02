from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from django.views import generic

#--- TemplateView
class HomeView(TemplateView):

    template_name = 'index.html'

def step1(request):
    return render(request, 'step1.html')
def step2(request):
    return render(request, 'step2.html')
def step3(request):
    return render(request, 'step3.html')
def step4(request):
    return render(request, 'step4.html')
def step5(request):
    return render(request, 'step5.html')
def step6(request):
    return render(request, 'step6.html')
