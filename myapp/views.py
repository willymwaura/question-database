
from django.http import HttpResponse
from django.shortcuts import render

from .models import Feature
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request,'index.html')

def search(request):
    word = request.POST.get('tex', '')
    if not word:
        return render(request, 'index.html')
    
    a = Feature(question=word)
    a.save()
    return redirect('all')
        

def all(request):
    data=Feature.objects.all()
    return render(request,'recent.html',{'value':data})
