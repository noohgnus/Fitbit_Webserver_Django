# Register your models here.
from django.contrib import admin

from .models import SurveyResult, User, Checkin

admin.site.register(User)
admin.site.register(SurveyResult)
admin.site.register(Checkin)
