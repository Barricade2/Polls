from django.forms import ModelForm, Form
from django import forms
from apps.polls.models import Poll, Question


class PollForm(ModelForm):
    class Meta:
        model=Poll
        fields=['title','plot','start_at','end_at', 'is_published']


class ContactForm(Form):
    name=forms.CharField(max_length=50, label="Наименование")
    artist=forms.CharField(max_length=50, label="Исполнитель")
    release=forms.IntegerField(label="Год публикации")
    price=forms.IntegerField(label="Стоимость")

class QuestionForm(ModelForm):
    class Meta:
        model=Question
        fields=['title','plot','type', 'poll', 'choice']

# class NameModelChoiceField(forms.ModelChoiceField):
#     def label_from_instance(self, obj):
#         return "%s"%obj.title

# class StudentForm(forms.Form):
#     title                     = forms.CharField(label='Название', max_length=256)
#     citizenship             = NameModelChoiceField(label = 'Гражданство',queryset  =  Citizenship.objects.order_by('-name'),initial = Citizenship.objects.get(id=1))
#     plot                     = forms.CharField(label='Описание', max_length=512)
#     start_at = forms.DateTimeField(label='Дата старта')
#     end_at =  forms.DateTimeField(label='Дата окончания')


