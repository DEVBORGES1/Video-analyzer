from django.shortcuts import render
from .models import Video
from django.http import HttpResponse
from .openai import Transcricao
# Create your views here.
def home(request):
    if request.method == "GET":
       return render(request, 'home.html')
    elif request.method == "POST":
        titulo = request.POST.get('titulo')
        video = request.FILES.get('video')
        
        video_opload = Video(titulo=titulo, video=video)
        video_opload.save()

        trascricao = Transcricao(video_opload.video.path)
        print(trascricao.transcrever())

        return HttpResponse('Deu certo')

