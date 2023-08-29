from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from .models import Survey, Question, Choice

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Usuario ya existe."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords NO Coinciden."})

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('index')

@login_required 
def index(request):
    #questions = Question.objects.all()
    surveys = Survey.objects.filter(active=True).order_by("pub_date")[:5]
    #return render(request, 'index.html', {'questions': questions})
    return render(request, 'index.html', {'surveys': surveys})

@login_required
def survey(request,pk):
    #question = Question.objects.get(id=pk)
    #options = question.choices.all()
    survey = Survey.objects.get(id=pk)
    options = Question.objects.filter(survey=pk)

    # for question in question:
    #   print(question.text)
    #   for choice in question.choice_set.all():
    #       print(choice.text)
    
    return render(request, 'survey.html', {'survey':survey, 'options': options })

@login_required
def vote(request,pk):
    question = Question.objects.get(id=pk)
    options = question.choices.all()
    
    return render(request, 'vote.html', {'question':question, 'options': options })

@login_required
def result(request, pk):
    question = Question.objects.get(id=pk)
    options = question.choices.all()
    if request.method == 'POST':
        inputvalue = request.POST['choice']
        selection_option = options.get(id=inputvalue)
        selection_option.vote += 1
        selection_option.save()
    return render(request, 'result.html', {'question': question, 'options': options})
