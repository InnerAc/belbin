from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from belbin.models import Student
from belbin.forms import RegisterForm
from belbin.forms import ExamForm
from django.core.exceptions import ObjectDoesNotExist
from belbin.function import toCharacter
# Create your views here.

def index(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		
		if form.is_valid():
			sid = request.POST['sid']
			tmp_stu = True
			try:
				stu = Student.objects.get(s_id = sid)
			except ObjectDoesNotExist:
				tmp_stu = False
			if tmp_stu:
				if stu.s_pwd == request.POST['spwd']		
					request.session['isLogin'] = True
				
	return render(request,'index.html',{'form': form})

def register(request):
	
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		
		if form.is_valid():
			sid = request.POST['sid']
			tmp_stu = False
			try:
				stu = Student.objects.get(s_id = sid)
				print 'exit()'
			except ObjectDoesNotExist:
				tmp_stu = True
			if tmp_stu:
				sname = request.POST['sname']
				spwd = request.POST['spwd']
				sphone = request.POST['sphone']
				semail = request.POST['semail']
				swechat = request.POST['swechat']
				sgrade = request.POST['sgrade']
				scollege = request.POST['scollege']
				
				stu = Student(s_id = sid)
				stu.s_name = sname
				stu.s_pwd = spwd
				stu.s_phone = sphone
				stu.s_email = semail
				stu.s_wechat = swechat
				stu.s_grade = sgrade
				stu.s_college = scollege
				stu.save()
				
				request.session['sid'] = sid
				
				return HttpResponseRedirect('/exam')
	form = RegisterForm()
	return render(request,'register.html',{'form': form})

def exam(request):
	if request.method == 'POST':
		form = ExamForm(request.POST)
		characters = {'CW':0,'CO':0,'SH':0,'PL':0,'RI':0,'ME':0,'TW':0,'FI':0}
		if form.is_valid():
			for i in range(1,8):
				tmp_check = 'check'+str(i)
				chara = request.POST[tmp_check]
				characters[chara] += 1
			for k,v in characters.items():
				if v == max(characters.values()):
					character = k
			sid = request.session.get('sid')
			stu = Student.objects.get(s_id = sid)
			stu.s_characters = character
			stu.save()
			print toCharacter.charaDict[character]
			return HttpResponseRedirect('/info/'+sid)
	form = ExamForm()
	return render(request,'exam.html',{'form': form})


def info(request,sid):
	try:
		stu = Student.objects.get(s_id = sid)
	except ObjectDoesNotExist:
		return HttpResponseRedirect('/')
	stu.s_characters = toCharacter.charaDict[stu.s_characters]
	return render(request,'info.html',{'stu': stu})
