import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    #useless fn for testing
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


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
    time = models.DateTimeField('checkintime')

    def __str__(self):
        return str(self.userid) + " / " + str(self.time)

class SurveyResult(models.Model):
    submit_user_id = models.IntegerField()
    submit_time = models.DateTimeField()
    q1 = models.IntegerField(default = -1)
    q2 = models.IntegerField(default = -1)
    q3 = models.IntegerField(default = -1)
    q4 = models.IntegerField(default = -1)
    q5 = models.IntegerField(default = -1)
    q6 = models.IntegerField(default = -1)
    q7 = models.IntegerField(default = -1)
    q8 = models.IntegerField(default = -1)
    q9 = models.IntegerField(default = -1)
    q10 = models.IntegerField(default = -1)
    q11 = models.IntegerField(default = -1)
    q12 = models.IntegerField(default = -1)
    q13 = models.IntegerField(default = -1)
    q14 = models.IntegerField(default = -1)
    q15 = models.IntegerField(default = -1)
    q16 = models.IntegerField(default = -1)
    q17 = models.IntegerField(default = -1)
    q18 = models.IntegerField(default = -1)
    q19 = models.IntegerField(default = -1)
    q20 = models.IntegerField(default = -1)
    q21 = models.IntegerField(default = -1)
    q22 = models.IntegerField(default = -1)
    q23 = models.IntegerField(default = -1)
    q24 = models.IntegerField(default = -1)
    q25 = models.IntegerField(default = -1)
    q26 = models.IntegerField(default = -1)
    q27 = models.IntegerField(default = -1)
    q28 = models.IntegerField(default = -1)
    q29 = models.IntegerField(default = -1)
    q30 = models.IntegerField(default = -1)
    q31 = models.IntegerField(default = -1)
    q32 = models.IntegerField(default = -1)
    q33 = models.IntegerField(default = -1)
    q34 = models.IntegerField(default = -1)
    q35 = models.IntegerField(default = -1)
    q36 = models.IntegerField(default = -1)

    def __str__(self):
        return "User: " + str(self.submit_user_id) + " / Submitted At: " + str(self.submit_time)
