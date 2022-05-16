from django.shortcuts import render
from .models import Question,Choice


def index(request):
    context = {"my_name":"Ngo Nguyen Hoang Dung"}
    return render(request,'polls/base.html',context)

def question(request):
    list_question = Question.objects.all()
    context = {"list_question":list_question}
    return render(request,'polls/question.html',context)

def choice(request,id_question):
    question = Question.objects.get(pk=id_question)
    list_choice = question.choice_set.all()
    return render(request,'polls/choice.html',{'question':question,'list_choice':list_choice})

def result(request,id_question):
    return render(request,'polls/results.html')
# Create your views here.
