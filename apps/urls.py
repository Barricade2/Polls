from django.urls import path, include

urlpatterns = [
    path('', include('apps.polls_login.urls')),
    path('polls/', include('apps.polls.urls')),
]