from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def berita1(request):
  template = loader.get_template('berita1.html')
  return HttpResponse(template.render())
def berita2(request):
  template = loader.get_template('berita2.html')
  return HttpResponse(template.render())


# Create your views here.
