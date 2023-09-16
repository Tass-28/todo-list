from django.shortcuts import render
from .models import Task

# Create your views here.
#def index(request):
   # return render(request,"todos.html",{'todos':[{'football':'completed'},{'django':'pending'}]})
def about(request):
   return render(request,'about.html') 
def index(request):
    tasks=list(Task.objects.all())
    return render(request,'todos.html',{"name":"tasneem","tasks":tasks})