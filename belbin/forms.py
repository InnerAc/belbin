#coding:utf-8
from django import forms

class RegisterForm(forms.Form):
	sid = forms.CharField(label = '学号')
	sname = forms.CharField(label = '姓名')
	spwd = forms.CharField(label = '密码',widget=forms.PasswordInput(attrs={'placeholder': '密码'}))
	sphone = forms.CharField(label = '手机')
	semail = forms.EmailField(label = '邮箱')
	swechat = forms.CharField(label = '微信')
	sgrade = forms.CharField(label = '年级')
	scollege = forms.CharField(label = '专业')

class ExamForm(forms.Form):
	RADIO_CHOICES1 = (
		('A','我能很快地发现并把握住新的机遇。'),
		('B','我能与各种类型的人一起合作共事。'),
		('C','我生来就爱出主意。'),
	)
	RADIO_CHOICES2 = (
		('A','如果会议没有得到很好的组织、控制和主持，我会感到不痛快。'),
		('B','我容易对那些有高见而又没有适当地发表出来的人表现得过于宽容。'),
		('C','只要集体在讨论新的观点，我总是说的太多。'),
	)
	check1 = forms.ChoiceField(label='一、我认为我能为团队做出贡献是',widget=forms.RadioSelect, choices=RADIO_CHOICES1)
	check2 = forms.ChoiceField(label='二、在团队中，我可能有的弱点是',widget=forms.RadioSelect, choices=RADIO_CHOICES2)