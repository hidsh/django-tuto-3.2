from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last 5 published"""
        return Question.bojects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (keyError, Choice.DoesNotExist):
        # エラー表示付きで投票フォームを再表示
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'you did not select a choice.',
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POSTデータを正常に処理した後は、常にHttpResponseRedirectを返す
        # これにより、ユーザーが[戻る]ボタンを押した場合にデータが2回投稿されるのを防ぐ
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

