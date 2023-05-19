from django.shortcuts import render

# Create your views here.
#HEADER PRESENTE EN TODAS LAS PAGINAS
def index(request):
    return render(request,"index.jinja2")