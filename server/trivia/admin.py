from django.contrib import admin

from .models import Question
from .models import Choice
from .models import Hint

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
    min_num = 1
    max_num = 3

class HintInline(admin.StackedInline):
    model = Hint
    extra = 3
    min_num = 0
    max_num = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text','answer_text']}),
    ]
    inlines = [ChoiceInline,HintInline]

admin.site.register(Question,QuestionAdmin)


