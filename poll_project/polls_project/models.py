from django.db import models
from django.utils import timezone


class Question(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id')
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    opened = models.BooleanField(default=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
