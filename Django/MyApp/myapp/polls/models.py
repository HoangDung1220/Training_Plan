from secrets import choice
from django.db import models
from matplotlib.pyplot import cla

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    time_pub = models.DateTimeField()

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)