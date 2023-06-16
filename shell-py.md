## # **Shell Py - Bd.**
py manage.py shell
    from polls.models import Question, Choice
    Question.objects.all() -> <QuerySet []>
    from django.utils import timezone
    q = Question(question_text="¿Cual es el mejor jugador del mundo?", pub_date=timezone.now())
    q.save()

## # **Metodo Filter **
Question.objects.filter(pk=1)
<QuerySet [<Question: ¿Cuál es el mejor curso de Platzi?>]>
Question.objects.filter(pk=2)
<QuerySet [<Question: ¿Quién es el mejor profesor de Platzi?>]>
Question.objects.filter(pk=4)
<QuerySet []>
Question.objects.filter(question_text__startswith='¿Cuál')
<QuerySet [<Question: ¿Cuál es el mejor curso de Platzi?>, <Question: ¿Cuál es la mejor escuela de Platzi?>]>
Question.objects.filter(pub_date__year=timezone.now().year)
<QuerySet [<Question: ¿Cuál es el mejor curso de Platzi?>, <Question: ¿Quién es el mejor profesor de Platzi?>, <Question: ¿Cuál es la mejor
escuela de Platzi?>]>