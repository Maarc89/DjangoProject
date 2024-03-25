from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from modelManagement.models import Person

def test(request):
    mymembers = Person.objects.all().values()
    template = loader.get_template('members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))
