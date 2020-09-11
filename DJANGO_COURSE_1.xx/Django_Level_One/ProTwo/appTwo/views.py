from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("<em>My Second Project</em>")
    return render(request,'index.html')

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'apptwo/help.html',context=helpdict)
