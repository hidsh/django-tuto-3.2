from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Choice, Question

def index(request):
    # return HttpResponse('hello world. your\'re at the polls index.')

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
            'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # return HttpResponse('You\'re looking at question %s.' % question_id)
    
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

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

