from django.shortcuts import render,HttpResponse
from models import Post

# Create your views here.

def write(req):
    if req.method == 'POST':
        title = req.POST.get('title')
        data = req.POST.get('field')
        if not data:
            return HttpResponse('NO DATA')


    pass







