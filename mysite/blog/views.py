from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import BlogPost

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("archive.html")
    c = {'posts':posts}
    return HttpResponse(t.render(c))
