from django.urls import path
from . import views
from .views import PollView, PollDetail, pollAdd

app_name = 'polls'
urlpatterns = [
    path('', PollView.as_view(), name='polls-list'),
    path('<int:pk>/question/', PollDetail.as_view(), name='poll-detail'),
    path('add/', views.pollAdd, name='poll-add'),
    path('<int:pk>/edit/', views.pollEdit, name='poll-edit'),
    path('<int:pk>/question/add/', views.questionAdd, name='question-add'),
    path('<int:pk>/question/<int:id>/edit/', views.questionEdit, name='question-edit'),
    path('<int:pk>/edit/update/', views.poll_put_, name='poll-put'),#временный метод для запроса в api
]