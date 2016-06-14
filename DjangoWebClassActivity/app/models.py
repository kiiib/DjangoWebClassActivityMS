"""
Definition of models.
"""

from django.db import models
from django import forms
from django.utils.timezone import localtime;

# Create your models here.
class Activity(models.Model):
    title = models.CharField(max_length = 20)
    date = models.DateField()
    address = models.CharField(max_length = 100)
    content = models.TextField(max_length = 50000)
    price = models.DecimalField(max_digits = 4, decimal_places = 0)
    deadline = models.DateField()    #報名時限
    imgurl = models.ImageField(upload_to='images/')
    author = models.CharField(max_length = 20)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['deadline']     #默認報名時間排序

class User(models.Model):
    Student = 'Student'
    Teacher = 'Teacher'
    IDENTITY_CHOICES = (
        (Student, 'Student'),
        (Teacher, 'Teacher'),
    )
    Male = 'Male'
    Female = 'Female'
    SEX_CHOICES = (
        (Male, 'Male'),
        (Female, 'Female'),
    )
    identity = models.CharField(max_length = 8, choices = IDENTITY_CHOICES, default = Student)
    id_number = models.CharField(max_length = 10)
    name = models.CharField(max_length = 20)
    sex = models.CharField(max_length = 5, choices = SEX_CHOICES, default = Student)
    tel = models.CharField(max_length = 12)
    email = models.EmailField(max_length = 30)
    password = models.CharField(max_length = 20)
    birthday = models.DateTimeField()

    def __unicode__(self):
        return self.name

class JOINT_ACTIVITY(models.Model):
    user_id = models.CharField(max_length = 5)
    act_id = models.CharField(max_length = 5)

    def __unicode__(self):
        return self.name