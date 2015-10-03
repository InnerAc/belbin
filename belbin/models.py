from django.db import models

# Create your models here.

class Student(models.Model):
	s_id = models.CharField(max_length=20)
	s_name = models.CharField(max_length=20)
	s_pwd = models.CharField(max_length=20)
	s_phone = models.CharField(max_length=20)
	s_email = models.EmailField()
	s_wechat = models.CharField(max_length=30)
	s_grade = models.CharField(max_length=4)
	s_college = models.CharField(max_length=100)
	s_characters = models.CharField(max_length=3)
	
	s_tid = models.CharField(max_length=20)

class Team3(models.Model):
	t3_name = models.CharField(max_length=20)
	one = models.CharField(max_length=20)
	two = models.CharField(max_length=20)
	three = models.CharField(max_length=20)
	
	t3_isfull = models.CharField(max_length=3)