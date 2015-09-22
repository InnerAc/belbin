from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from belbin.models import Student
from belbin.forms import RegisterForm
from belbin.forms import ExamForm
from belbin.forms import LoginForm
from belbin.function import Team
from django.core.exceptions import ObjectDoesNotExist
from belbin.function import toCharacter


def isLogin(request):
	if request.session.get('isLogin'):
		sid = request.session.get('sid') 
		return True
	else:
		return False

def match3(request):
	if isLogin(request):
		pass
	else:
		return HttpResponseRedirect('/')
	sid = request.session.get('sid')
	stu = Student.objects.get(s_id = sid)
	chara = stu.s_characters
	lists = ['one','two','three']
	is_select = False
	for li in lists:
		for cha in Team.team3[li]:
			if(chara == cha):
				is_select = True
		if(is_select):
			break
	print li
	return HttpResponseRedirect('/')