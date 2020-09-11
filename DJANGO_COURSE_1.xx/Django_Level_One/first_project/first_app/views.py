from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # insert_me is a template tag in templates/first_app/index.html
    # my_dict = {'insert_me':"Now I am coming from first_app/index.html!"}
    # return render(request,'first_app/index.html',context=my_dict)
    # return HttpResponse("hello world")
    return render(request,'index.html')

def first_app(request):
    # insert_me is a template tag in templates/first_app/index.html
    my_dict = {'insert_me':"Now I am coming from first_app/index.html!"}
    return render(request,'first_app/index.html',context=my_dict)
