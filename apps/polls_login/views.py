from django.shortcuts import render, redirect

from apps.polls.models import UserChoiceID
from apps.polls_login.forms import UserLoginForm
from django.contrib.auth import login


def index(request):
	return render(request, 'polls_login/index.html')

def user_login(request):
	if request.method == 'POST':
		form = UserLoginForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('polls:polls-list')
	else:
		form = UserLoginForm()
	return render(request, 'polls_login/login.html', {"form": form})


def result(request, user_id):
	user = UserChoiceID.objects.get(pk=user_id)
	context = {"user":user}
	return render(request, 'polls_login/result.html', context)