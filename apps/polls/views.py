from django.shortcuts import  redirect
import requests
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Poll, Question
from .forms import PollForm, QuestionForm


class PollView(ListView):
    model = Poll
    template_name = 'polls/polls_list.html'
    context_object_name = 'polls'
    queryset = Poll.objects.filter(is_published=True)

class PollDetail(DetailView):
    model = Poll
    template_name = 'polls/polls_detail.html'
    context_object_name = 'poll'
    queryset = Poll.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        ctx = super(PollDetail, self).get_context_data(**kwargs)
        ctx['questions'] = Question.objects.filter(poll=self.kwargs.get('pk'))
        return ctx


def pollAdd(request):  # Форма записи в БД
    pollForm = PollForm
    context = {"pollForm": pollForm, }
    return render(request, "polls/polls_add.html", context)

def pollEdit(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    pollForm=PollForm(instance=poll)
    context = {"pollForm":pollForm, "pk":pk,}
    return render(request, "polls/polls_edit.html", context)

def questionAdd(request, pk):  # Форма записи в БД
    questionForm = QuestionForm
    context = {"questionForm": questionForm, 'pk':pk, }
    return render(request, "question/question_add.html", context)

def questionEdit(request, pk, id):
    #poll = get_object_or_404(Poll, pk=pk)
    question = get_object_or_404(Question, pk=id)
    questionForm=QuestionForm(instance=question)
    context = {"questionForm":questionForm, "pk":pk,"id":id }
    return render(request, "question/question_edit.html", context)

@csrf_exempt
def poll_put_(request, pk): #Временная обработчик, звамен Ajax
    URL = 'http://127.0.0.1:8000/api/v1/polls/pollssinglId/1/'
    r = requests.put(URL, data=request.POST, headers=dict(Referer=URL))
    return redirect('polls:polls-list')
