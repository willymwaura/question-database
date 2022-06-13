
from django.http import HttpResponse
from django.shortcuts import render ,redirect

from .models import Feature
import string

# Create your views here.
def index(request):
    return render(request,'index.html')

def search(request):
        word=request.POST['tex']
        word=word.strip()
        word=word.lstrip()
        a=Feature(question=word)
        b=len(word)
        print(b)
        if b== 0 :
            return HttpResponse("kindly enter some data")
        
        else:
            a.save()
            return redirect("all")
        

def all(request):
    data=Feature.objects.all()
    return render(request,'recent.html',{'value':data})
