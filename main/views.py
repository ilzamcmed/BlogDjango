from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Postagem
from django.views import generic
# Create your views here.

def home(request):
    
    template = loader.get_template('main/home.html')
    postagem_list = Postagem.objects.order_by('-data')[:3]
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None
    context = {
        "username": username,
         "postagem_list": postagem_list,
    } 
    return HttpResponse(template.render(context, request))

def conselhojedi(request):
    template = loader.get_template('main/conselhojedi.html')
    context = {}
    return HttpResponse(template.render(context, request))

def terapiaintensiva(request):
    template = loader.get_template('main/terapiaintensiva.html')
    context = {}
    return HttpResponse(template.render(context, request))

def novidades(request):
    template = loader.get_template('main/novidades.html')
    postagem_list = Postagem.objects.order_by('-data')
    context = {
        "postagem_list": postagem_list,
    }
    return HttpResponse(template.render(context, request))

class PostDetail(generic.DetailView):
    model = Postagem
    template_name = 'main/post_detail.html'

def cursos(request):
    template = loader.get_template('main/cursos.html')
    context = {}
    return HttpResponse(template.render(context, request))

def cadastrar_usuario(request):
    form = UsuarioForm()
    return render(request, "home.html", {'form':form})