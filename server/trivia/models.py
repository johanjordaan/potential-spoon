from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answer_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text

class Hint(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    hint_text = models.CharField(max_length=200)

    def __str__(self):
        return self.hint_text