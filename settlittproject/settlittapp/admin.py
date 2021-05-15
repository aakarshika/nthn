from django.contrib import admin

from .models import Question, QuestionSet, Response, Photo, Voter, User

admin.site.register(Question)
admin.site.register(QuestionSet)
admin.site.register(Response)
admin.site.register(Photo)
admin.site.register(Voter)
admin.site.register(User)