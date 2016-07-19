from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404
from django.shortcuts import get_object_or_404
from django.template import RequestContext,loader

from .models import Question


def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    template=loader.get_template('polls/index.html')
    context=RequestContext(request,{'latest_question_list':latest_question_list})
    return HttpResponse(template.render(context))

def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    template=loader.get_template('polls/detail.html')
    context=RequestContext(request,{})
    return HttpResponse('you are looking at question %s'%question_id)

def results(request,question_id):
    response='you aer looking at the result of question %s'
    return HttpResponse(response %question_id)

def vote(request,question_id):
    return HttpResponse('you are voting on question %s'%question_id)