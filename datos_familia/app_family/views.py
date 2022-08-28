from django.http import HttpResponse
from django.template import Template, Context, loader
from app_family.models import family

# Create your views here.

def template1 (request):
    queryset = family.objects.all()
    diccionario = {"app_family": queryset}
    plantilla = loader.get_template("plantilla1.html")
    documento_html = plantilla.render(diccionario)

    return HttpResponse(documento_html)