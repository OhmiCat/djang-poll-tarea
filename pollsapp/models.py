from django.db import models

# Create your models here.

class Survey(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published', null=True)
    

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    option = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.option
