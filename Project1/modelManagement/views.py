from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from modelManagement.models import Politic, PartitPolitic, Reunio

def test(request):
    mymembers = Politic.objects.all().values()
    template = loader.get_template('politics.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))
def politics(request):
    politics = Politic.objects.all().values()
    template = loader.get_template('politics.html')
    context = {
        'politics': politics,
    }
def partit_politic(request):
    partits = PartitPolitic.objects.all().values()
    template = loader.get_template('partitspolitics.html')
    context = {
        'partits_politics': partits,
    }
def reunio(request):
    reunions = Reunio.objects.all().values()
    template = loader.get_template('reunions.html')
    context = {
        'reunions': reunions,
    }