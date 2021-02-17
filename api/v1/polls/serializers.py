from rest_framework import serializers
from apps.polls.models import Poll, Question, Choice, UserChoiceID


#
class ChoiceSerializer(serializers.ModelSerializer):
    """
            Серилизатор подборки
        text=текст перечней
    """
    class Meta:
        model = Choice
        fields = ('id','text')

class QuestionSerializer(serializers.ModelSerializer):
    """
                Серилизатор вопросов, choice=текст перечней,
            "title": навзание,
            "plot": описание,
            "choice": перечни

    """
    choice = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id','title','plot','type','choice')

class PollSerializer(serializers.ModelSerializer):
    """
                    Серилизатор опросов, общий, question-вопросы к опросу
                "title": навзание,
                "plot": описание,
                "start_at": начала,
                "end_at": конец,
                "is_published": опубликован,
                "question": вопросы

    """
    question = QuestionSerializer(many=True, source='poll')

    class Meta:
        model = Poll
        fields = ('id','title','plot','start_at','end_at','is_published', 'question')
#


class PollSinglSerializer(serializers.ModelSerializer):
    """
                    Серилизатор опросов
                "title": навзание,
                "plot": описание,
                "start_at": начала,
                "end_at": конец,
                "is_published": опубликован,

    """
    class Meta:
        model = Poll
        fields = ('id','title','plot','start_at','end_at','is_published')

class QuestionSinglSerializer(serializers.ModelSerializer):
    """
                        Серилизатор вопросов
            "title": навзание,
            "plot": описание,
            "choice": перечни
    """

    class Meta:
        model = Question
        fields = ('id','title','plot','type','poll', 'choice')

        def create(self, request):
            result = request.pop("poll")
            question = Question.objects.create(poll=result, **request)
            return question




class WriteUserChoiceIDSerializer(serializers.ModelSerializer):
    """
        Серилизатор запись пользователей с их ответами на вопросы
    """
    class Meta:
        model = UserChoiceID
        fields = ('id','uuid','poll','question','choice')







# class ListUserChoiceIDSerializer(serializers.ModelSerializer):
#     """
#         Серилизатор список пользователей с их ответами на вопросы
#     "id": id пользователя,
#     "uuid": уникальеый инд. пользователя,
#     "poll": опроса,
#     "question": вопрос,
#     "choice": выбор
#     """
#     choice = ChoiceSerializer(many=True)
#     poll = QuestionSerializer(source='poll')
#     question = PollSerializer(many=True, source='question')
#
#     class Meta:
#         model = UserChoiceID
#         fields = ('id','uuid','poll','question','choice')

