from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.views.generic.dates import DayArchiveView
from django.views.generic import ListView, DetailView

# def index(request):
#     lastest_question_list = Question.objects.all()
#     return render(request, "polls/index.html", {
#         "latest_question_list": lastest_question_list
#     })
#     # return HttpResponse("Hello World, Polls")

class ListQuestion(ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    # queryset = Question.objects.all()
    queryset = Question.objects.order_by("pub_date")[:5]
    # queryset = Question.objects.order_by("-pub_date")[:5]

# class ListQuestion(ListView):
#     template_name = "polls/index.html"
#     context_object_name = "latest_question_list"

#     def get_queryset(self):
#         return Question.objects.order_by("-pub_date") [:5]

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {
#         'question': question
#     })
#     # return HttpResponse(f"Estas viendo la pregunta numero {question_id}")

class DetailView(DetailView):
    model = Question
    template_name = "polls/detail.html"

# def results(request, question_id):
#     # return HttpResponse(f"Estas viendo los resultados de la pregunta numero {question_id}")
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {
#         'question': question
#     })

class ResultView(DetailView):
    template_name = "polls/results.html"

def vote(request, question_id):
    # return HttpResponse(f"Estas votando a la pregunta numero {question_id}")
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_menssage': 'No elegiste una respuesta'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class QuestionDayArchiveView(DayArchiveView):
    queryset = Question.objects.all()
    date_field = 'pub_date'
    allow_empty = True
