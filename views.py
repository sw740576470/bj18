from djiango.http import HttpREsponse
from djiango.shortcuts import redirect

def index(request)
    return HttpResponse('index')

def login(request)
    return redirect('/index'/)
