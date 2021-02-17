from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PollViewSet, PollSinglListCreate, QuestionSinglListCreate, PollSinglUpdateDestroyAPIView, \
    QuestionSinglUpdateDestroyAPIView, WriteUserChoiceIDSinglUpdateDestroyAPIView

#router = DefaultRouter()
#router.register(r'apipolls', PollViewSet, basename='apipolls')

urlpatterns = [
    #path('', include(router.urls),),
    path('pollsapi/', PollViewSet.as_view(), name='pollsapi'),
    path('pollssingl/', PollSinglListCreate.as_view(), name='pollssingl'),
    path('questionsingl/', QuestionSinglListCreate.as_view(), name='questionsingl'),
    path('pollssinglId/<int:pk>/', PollSinglUpdateDestroyAPIView.as_view(), name='pollssinglId'),
    path('questionsinglId/<int:pk>/', QuestionSinglUpdateDestroyAPIView.as_view(), name='questionsinglId'),
    path('userchoicesingl/<int:pk>/', WriteUserChoiceIDSinglUpdateDestroyAPIView.as_view(), name='userchoicesingl'),
    #path('userchoiceapi/', ListUserChoiceIDList.as_view(), name='userchoiceapi'),
]
