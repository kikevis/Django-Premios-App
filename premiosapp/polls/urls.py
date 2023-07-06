from django.urls import path
from . import views

from django.views.generic.dates import ArchiveIndexView
from polls.models import Question

app_name = "polls"
urlpatterns = [
    #ex: /polls/
    # path(
    #     "",
    #     views.index,
    #     name="index"
    # ),

    #ex: /polls/ ListView
    path(
        '',
        views.ListQuestion.as_view(),
        name='index'
    ),

    #ex: /polls/1/
    path(
        # "<int:question_id>/detail/",
        "<int:pk>/detail/",
        views.DetailView.as_view(),
        name="detail"
    ),

    #ex: /polls/1/results
    path(
        # "<int:question_id>/results/",
        "<int:pk>/results/",
        views.ResultView.as_view(),
        name="results"
    ),

    #ex: /polls/1/vote
    path(
        "<int:question_id>/vote/",
        views.vote,
        name="vote"
    ),

    #ex: 2023/jun/8 and 2023/jun/14
    path(
        "<int:year>/<str:month>/<int:day>/",
        views.QuestionDayArchiveView.as_view(),
        name="question archive day"
    ),

    #ex: /polls/prueba DayArchiveView
    path(
        'prueba/',
        ArchiveIndexView.as_view(model=Question, date_field="pub_date"),
        name="article_archive.html"
    ),
]