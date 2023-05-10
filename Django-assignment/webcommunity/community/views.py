from django.shortcuts import render, redirect, get_object_or_404
from .models import Novel

def home(request):
    novels = Novel.objects.all()
    return render(request, 'home.html', {'novels':novels})

def detail(request, id):
    novel = get_object_or_404(Novel, pk = id)
    return render(request, 'detail.html', {'novel':novel})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_novel = Novel()
    new_novel.title = request.POST['title']
    new_novel.author = request.POST['author']
    new_novel.rating = request.POST['rating']
    new_novel.body = request.POST['body']
    new_novel.save()
    return redirect('detail', new_novel.id)