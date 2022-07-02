from json import load
from multiprocessing import context
from re import template
from unittest import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .forms import SubmitedCode

from .models import User,Problem,Test_cases,Submission

def problems(request):
    problem_list = Problem.objects.all()
    template = loader.get_template('OJ/problems.html')
    context = {'problem_list': problem_list}
    return HttpResponse(template.render(context,request))

def problem_details(request, question_name):
    problem = get_object_or_404(Problem,prob_name=question_name)
    if request.method == 'POST':
        form = SubmitedCode(request.POST)
        if form.is_valid():
            code = form.cleaned_data['solution']
            print(code)
    else:
        form = SubmitedCode()
    template = loader.get_template('OJ/detail.html')
    context = {'problem':problem,'form':form}
    return HttpResponse(template.render(context,request))





