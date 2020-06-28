from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Postagem
from .forms import CommentForm
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

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Postagem, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})