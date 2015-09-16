from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from belbin.models import Student
from belbin.forms import RegisterForm
from belbin.forms import ExamForm
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def index(request):
	return render(request,'index.html')

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
			return HttpResponseRedirect('/')
	form = ExamForm()
	print 'ahhhh'
	return render(request,'exam.html',{'form': form})