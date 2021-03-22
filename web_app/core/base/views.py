from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView

from django.core.mail import send_mail

# Create your views here.
class IndexTemplateview(TemplateView):
    template_name = r'base/index.html'


class ContactTemplateView(TemplateView):
    template_name = r'base/base.html'

    def post(self, request, *args, **kwargs):
        print(request.POST.get('name', None))
        print(request.POST.get('email', None))
        print(request.POST.get('subject', None))
        print(request.POST.get('message', None))
        return HttpResponse('Correo, enviado')

def prueba(request):
    return render(request, 
                 'base/base.html', 
                  context ={})