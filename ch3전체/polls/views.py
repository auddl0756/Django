from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from polls.models import Choice,Question
# Create your views here.

#index.html이라는 템플릿을 사용하는 함수
def index(request):
    latest_question_list  = Question.objects.all().order_by('-published_date')[:5]
    context = {'latest_question_list' : latest_question_list}
    return render(request,'polls/index.html',context)

#detail.html이라는 템플릿을 사용하는 함수
def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})


#폼으로부터 수신한 POST 데이터를 처리하는 함수
def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(reuqest,'polls/detail.html',{
            'question':question,
            'error_message':"you didn't select a choice.",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))


#폼 데이터 처리 결과를 보여주는 함수
def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})
    