from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

from django.shortcuts import redirect
from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic import TemplateView

# Create your views here.
class IndexTemplateview(TemplateView):
    template_name = r'base/index.html'


class ContactTemplateView(TemplateView):
    template_name = r'base/base.html'

    def post(self, request, *args, **kwargs):
        subject = str(request.POST.get('subject', None))
        message = str(request.POST.get('message', None)) + '\n\n Correo: ' + str(request.POST.get('email', None)) + '\n Cliente: ' +  str(request.POST.get('name', None))
        recipient_list = ['andresferro6@hotmail.com']
        
        try:
            send_mail(subject, message, f'FamotorsTuning - Taller <{settings.EMAIL_HOST_USER}>' , recipient_list)
            messages.success(request, 'Correo enviado exitosamenete')
        except:
            messages.error(request, 'No fue posible enviar el mensaje, intenta de nuevo')
        return redirect('base:index')

def prueba(request):
    return render(request, 
                 'base/base.html', 
                  context ={})