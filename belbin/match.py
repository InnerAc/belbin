from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from belbin.models import Student
from belbin.models import Team3
from belbin.forms import MatchForm
from belbin.function import Team
from django.core.exceptions import ObjectDoesNotExist
from belbin.function import toCharacter


def isLogin(request):
	if request.session.get('isLogin'):
		return True
	else:
		return False

def match(request):
	if isLogin(request):
		pass
	else:
		return HttpResponseRedirect('/')
	
	if request.method == 'POST':
		form = MatchForm(request.POST)
		if form.is_valid():
			num = request.POST['t_num']
			types = request.POST['t_type']
			print num,types
			if num == '3':
				match3(request,types)
	form = MatchForm()
	return render(request,'form.html',{'form': form})

def match3(request,types):
	sid = request.session.get('sid')
	stu = Student.objects.get(s_id = sid)
	chara = stu.s_characters
	lists = ['one','two','three']
	canlists = []
	is_select = False
	for li in lists:
		is_select = False
		for cha in Team.team3[li]:
			if(chara == cha):
				is_select = True
		if(is_select):
			canlists.append(li)
	print canlists
	
	# Start match
	isok = True
	for can in canlists:
		if(can == 'one'):
			teams = Team3.objects.filter(one = '',t3_name = types)
			if teams:
				team = teams[0]
				team.one = sid
				stu.s_tid = team.id
				team.save()
				stu.save()
				isok = False
				break;
			else:
				continue
		elif can == 'two':
			teams = Team3.objects.filter(two = '',t3_name = types)
			if teams:
				team = teams[0]
				team.two = sid
				stu.s_tid = team.id
				team.save()
				stu.save()
				isok = False
				break;
			else:
				continue
		elif can == 'three':
			teams = Team3.objects.filter(three = '',t3_name = types)
			if teams:
				team = teams[0]
				team.three = sid
				stu.s_tid = team.id
				team.save()
				stu.save()
				isok = False
				break;
			else:
				continue
	if isok:
		team = Team3.objects.create(t3_name = types)
		can = canlists[0]
		if(can == 'one'):
			team.one = sid
		elif can == 'two':
			team.two = sid
		elif can == 'three':
			team.three = sid
		team.save()
		stu.s_tid = team.id
		stu.save()
	return HttpResponseRedirect('/')