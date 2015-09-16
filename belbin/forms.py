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