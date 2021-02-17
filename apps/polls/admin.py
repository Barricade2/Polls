from django.contrib import admin
from .models import Poll, Question, Choice, UserChoiceID


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    show_change_link = True


class PollAdmin(admin.ModelAdmin):
    fields = []
    list_display = ['title']
    search_fields = ['title']
    inlines = [QuestionInline]


    def get_readonly_fields(self, request, obj=None):
        if ((obj and obj.start_at)):
            readonly = ("start_at",)
            return (readonly)
        else:
            return super(PollAdmin, self).get_readonly_fields(request, obj)


admin.site.register(Poll, PollAdmin)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(UserChoiceID)