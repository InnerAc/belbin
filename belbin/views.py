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
				# character = request.POST['character']
				
				stu = Student(s_id = sid)
				stu.s_name = sname
				stu.s_pwd = spwd
				stu.s_phone = sphone
				stu.s_email = semail
				stu.s_wechat = swechat
				stu.s_grade = sgrade
				stu.s_college = scollege
				# stu.s_characters = character
				stu.save()
				print 'success'
				return HttpResponse(u"register success")
	form = RegisterForm()
	return render(request,'register.html',{'form': form})

def exam(request):
	if request.method == 'POST':
		form = ExamForm(request.POST)
		if form.is_valid():
			one = request.POST['check1']
			two = request.POST['check2']
			print one,two
			return HttpResponse(one+two)
	form = ExamForm()
	return render(request,'exam.html',{'form': form})