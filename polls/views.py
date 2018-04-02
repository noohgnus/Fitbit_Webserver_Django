from django.http import Http404
from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template import loader
from django.views import generic
from django.utils import timezone


from .models import Choice, Question, User, SurveyResult

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class UserView(generic.DetailView):
    model = User
    template_name = 'polls/user.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def ping(request, user_id):
    return HttpResponse("Pinged with %s." % user_id)

def submit_survey(request, user_id, survey_string):
    if(len(survey_string) != 36 or not survey_string.isdigit()):
        return HttpResponse("Invalid survey submission %s." % survey_string)

    s = survey_string
    survey_result = SurveyResult(
        submit_user_id = user_id,
        submit_time = timezone.now(),
        q1 = int(s[0]),
        q2 = int(s[1]),
        q3 = int(s[2]),
        q4 = int(s[3]),
        q5 = int(s[4]),
        q6 = int(s[5]),
        q7 = int(s[6]),
        q8 = int(s[7]),
        q9 = int(s[8]),
        q10 = int(s[9]),
        q11 = int(s[10]),
        q12 = int(s[11]),
        q13 = int(s[12]),
        q14 = int(s[13]),
        q15 = int(s[14]),
        q16 = int(s[15]),
        q17 = int(s[16]),
        q18 = int(s[17]),
        q19 = int(s[18]),
        q20 = int(s[19]),
        q21 = int(s[20]),
        q22 = int(s[21]),
        q23 = int(s[22]),
        q24 = int(s[23]),
        q25 = int(s[24]),
        q26 = int(s[25]),
        q27 = int(s[26]),
        q28 = int(s[27]),
        q29 = int(s[28]),
        q30 = int(s[29]),
        q31 = int(s[30]),
        q32 = int(s[31]),
        q33 = int(s[32]),
        q34 = int(s[33]),
        q35 = int(s[34]),
        q36 = int(s[35])
    )
    survey_result.save()

    return HttpResponse("submit with %s." % survey_string)
