from django.contrib import admin
from .models import Choice ,Question

# register questions
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

# enable Question input on admin page
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)