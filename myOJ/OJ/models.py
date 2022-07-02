from django.db import models
from django.forms import CharField

class User(models.Model):
    user_name = models.CharField(max_length=100)
    total_score = models.IntegerField(default=0)

class Problem(models.Model):
    prob_name = models.CharField(max_length=100)
    prob_desc = models.CharField(max_length=10000)
    prob_diff = models.CharField(max_length=50)
    solve_status = models.CharField(max_length=10)
    score = models.FloatField(default=0) 

    def __str__(self):
        return self.prob_name 

class Test_cases(models.Model):
    probId = models.ForeignKey(Problem,on_delete=models.CASCADE)
    input = models.CharField(max_length=10000)
    output = models.CharField(max_length=10000)

class Submission(models.Model):
    probId = models.ForeignKey(Problem,on_delete=models.CASCADE)
    timestrap = models.DateTimeField(auto_now_add=True)



