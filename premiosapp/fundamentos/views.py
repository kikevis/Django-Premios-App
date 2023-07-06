from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # lastest_question_list = Question.objects.all()
    # return render(request, "polls/index.html", {
    #     "latest_question_list": lastest_question_list
    # })
    # return HttpResponse("Hello World, Fundamentos")
    return render(request, "fundamentos/index.html", {
    })