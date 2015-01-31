from django.db import models

"""
There is currently only one space of questions.
Users are only strings; the plan is to associate with sessions.
"""


class Question(models.Model):
    user = models.CharField(max_length=32)
    text = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.user + ' - ' + self.text[:32]


class Answer(models.Model):
    question = models.ForeignKey(Question)
    user = models.CharField(max_length=32)
    text = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.user + ' - ' + self.text[:32]
