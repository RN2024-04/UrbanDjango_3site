from django.shortcuts import render
from django.views.generic import TemplateView



# Create your views here.
def platform_templates(request):
    return render(request, 'third_task/platform.html')

class games_templates(TemplateView):
    template_name = 'third_task/games.html'

class cart_templates(TemplateView):
    template_name = 'third_task/cart.html'