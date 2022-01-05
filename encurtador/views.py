from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, FormView, RedirectView, DetailView
from .models import Encurtador
from .forms import EncurtadorForm

# Create your views here.

class IndexView(FormView):
    template_name = 'encurtador/index.html'
    form_class = EncurtadorForm


def link_encurtado(request):
    if request.method == 'POST':
        original = request.POST.get('link_original')
        curto = request.POST.get('link_encurtado')
        try:
            encurtador = Encurtador.objects.create(
                link_original=original,
                link_encurtado=curto
            )
            encurtador.save()
        except:
            encurtador = Encurtador.objects.get(link_original=original)

        print(encurtador)

    return render(request, 'encurtador/encurtado.html', {'link_curto':encurtador})


def redirect_view(request, link_curto):
    encurtador = Encurtador.objects.filter(link_encurtado=link_curto).values()
    link_original = encurtador[0].get('link_original')
    if 'http://' in link_original or 'https://' in link_original:
        return redirect(f"{link_original}")

    return redirect(f"https://{link_original}")
    
