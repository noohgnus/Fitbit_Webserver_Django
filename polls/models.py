import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class User(models.Model):
    userid = models.IntegerField(unique=True)
    iscontrol = models.BooleanField(default=True)
    lastlogin = models.DateTimeField('lastlogin')

    def __str__(self):
        return str(self.userid) + " / " + str(self.lastlogin)


class Checkin(models.Model):
    userid = models.IntegerField(unique=False)
    ping_type = models.IntegerField(default=0)
    time = models.DateTimeField()

    def __str__(self):
        return "User : " + str(self.userid) + " / Check-in Type: " + str(self.ping_type) + " / Time: " + str(self.time)


class SurveyCompactResult(models.Model):
    submit_user_id = models.IntegerField()
    submit_time = models.DateTimeField()
    answer_sequence = models.CharField(max_length=128)

    def __str__(self):
        return str(self.submit_user_id) + " / " + str(self.submit_time) + " / " + str(self.answer_sequence)

class ReminderSubscription(models.Model):
    user_id = models.IntegerField()
    preferred_time = models.CharField(max_length=64)
    token = models.CharField(max_length=128)

    def __str__(self):
        return "user_id: %s / preferred_time: %s / token: %s" % (str(self.user_id), str(self.preferred_time), str(self.token))
        


class FeedbackData(models.Model):
    user_id = models.IntegerField()
    week = models.IntegerField()
    avg_weight = models.FloatField()
    avg_steps = models.FloatField()
    total_active_min = models.IntegerField()
    height = models.FloatField()

    def __str__(self):
        return "user: " + str(self.user_id) + " {week " + str(self.week) + "; " + \
               "avg_weight: " + str(self.avg_weight) + "; avg_steps: " + str(self.avg_steps) + \
               "; total_active_min: " + str(self.total_active_min) + "; height: " + str(self.height)
