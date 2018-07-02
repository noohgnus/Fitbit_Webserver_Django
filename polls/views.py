from django.http import Http404
from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.template import loader
from django.views import generic
from django.utils import timezone
from django.core import serializers


from .models import Choice, Question, User, SurveyCompactResult, Checkin, FeedbackData

from django.utils.dateparse import parse_datetime
import pytz
import datetime

tz = pytz.timezone('America/New_York')


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


def checkin(request, user_id, ping_type):
    check_in_data = Checkin(userid = user_id, ping_type = ping_type, time = timezone.now())
    check_in_data.save()
    return HttpResponse("User %s checked in." % str(user_id))


def get_checkins_yesterday(request):
    today = datetime.datetime.today().replace(hour=4, minute=0, second=0)
    yesterday = today - datetime.timedelta(days=1)
    # yesterday.replace(hour=0, minute=0, second=0)

    filter_results = Checkin.objects.filter(time__gte=yesterday, time__lte=today)
    # data_json = serializers.serialize("json", results, fields=())
    result_values = filter_results.values()

    return JsonResponse({"Checkins" : list(result_values)})


def get_surveys_yesterday(request):
    today = datetime.datetime.today().replace(hour=4, minute=0, second=0)
    yesterday = today - datetime.timedelta(days=1)
    # yesterday.replace(hour=0, minute=0, second=0)

    filter_results = SurveyCompactResult.objects.filter(submit_time__gte=yesterday, submit_time__lte=today)
    # data_json = serializers.serialize("json", results, fields=())
    result_values = filter_results.values()

    return JsonResponse({"Surveys" : list(result_values)})


def clear_data_before_yesterday(request):
    yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
    yesterday.replace(hour=0, minute=0, second=0)

    filter_results = SurveyCompactResult.objects.filter(submit_time__lte=yesterday)
    filter_results.delete()

    return HttpResponse("Flush complete.")


def submit_survey_compact(request, user_id, survey_string):
    if(len(survey_string) != 36 or not survey_string.isdigit()):
        return HttpResponse("Invalid survey submission %s." % survey_string)
    survey_result = SurveyCompactResult(
        submit_user_id = user_id,
        submit_time = datetime.datetime.now(tz),
        answer_sequence = survey_string)
    survey_result.save()
    return HttpResponse("Submitted with %s." % survey_result)


def submit_feedback(request, user_id, week, avg_weight, avg_steps, total_active_min, height):
    try:
        feedback_data = FeedbackData(
            user_id=user_id,
            week=week,
            avg_weight=avg_weight,
            avg_steps=avg_steps,
            total_active_min=total_active_min,
            height=height
        )
        feedback_data.save()
        return HttpResponse("Feedback successfully inserted.")
    except Exception as e:
        print(e)
        return HttpResponse("Invalid feedback format.")


def get_feedback(request, user_id):
    filter_results = FeedbackData.objects.filter(user_id=user_id)
    result_values = filter_results.values()

    return JsonResponse({"FeedbackData" : list(result_values)})

def remove_feedback(request, user_id):
    filter_results = FeedbackData.objects.filter(user_id=user_id).delete()
    return JsonResponse({"status":"complete"})

