# Register your models here.
from django.contrib import admin

from .models import SurveyResult
from .models import User

admin.site.register(User)
admin.site.register(SurveyResult)
