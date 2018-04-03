from django.contrib import admin

from .models import Question, Choice


# Register your models here.

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    #That adds a “Filter” sidebar that lets people filter the change list by the pub_date field:
    list_filter = ['pub_date']

    #adds a search box at the top of the change list
    search_fields = ['question_text']

    fieldsets = [
        (None,              {'fields': ['question_text']}),
        ('Data information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

# admin.site.register(Question)
# admin.site.register(Choice)
