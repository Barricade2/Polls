from rest_framework import viewsets, status, permissions, generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.polls.models import Poll, Question, UserChoiceID
from api.v1.polls.serializers import PollSerializer, PollSinglSerializer, QuestionSinglSerializer, WriteUserChoiceIDSerializer


"""Полное документация на Swagger 
"""
class PollViewSet(generics.ListAPIView):
    """Полный список расширенний.
    """
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    permission_classes = [permissions.AllowAny]



class PollSinglListCreate(generics.ListCreateAPIView):
    """Список и запись только опросов"""
    permission_classes = [permissions.AllowAny]
    queryset = Poll.objects.all()
    serializer_class = PollSinglSerializer

class QuestionSinglListCreate(generics.ListCreateAPIView):
    """Список и запись вопросов с приявзкой к опросам и перечням"""
    permission_classes = [permissions.AllowAny]
    queryset = Question.objects.all()
    serializer_class = QuestionSinglSerializer


class PollSinglUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Изменение, удаление опроса.
    """
    permission_classes = [permissions.AllowAny]
    queryset = Poll.objects.all()
    serializer_class = PollSinglSerializer
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class QuestionSinglUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Изменение, удаление вопроса.
    """
    permission_classes = [permissions.AllowAny]
    queryset = Question.objects.all()
    serializer_class = QuestionSinglSerializer
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class WriteUserChoiceIDSinglUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
        Получить, Измененить, Удалить от пользователя данные тестов.
    "poll": id опроса,
    "question": id вопроса,
    "choice": id перечней
    """
    permission_classes = [permissions.AllowAny]
    queryset = UserChoiceID.objects.all()
    serializer_class = WriteUserChoiceIDSerializer



# class ListUserChoiceIDList(generics.ListAPIView):
#     """Полный список пользователей.
#     """
#     serializer_class = ListUserChoiceIDSerializer
#     queryset = UserChoiceID.objects.all()
#     permission_classes = [permissions.AllowAny]
