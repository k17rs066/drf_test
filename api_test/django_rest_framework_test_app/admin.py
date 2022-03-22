from django.contrib import admin

from .models import User,QuestionEntry

admin.site.register(User)
admin.site.register(QuestionEntry)