# Register your models here.
from django.contrib import admin

from .models import Question
from .models import User

admin.site.register(Question)
admin.site.register(User)
