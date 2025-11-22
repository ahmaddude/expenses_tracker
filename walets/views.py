from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log them in immediately
            return redirect('/')  # redirect wherever you want
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def index(request):
    expensess = expenss.objects.filter(user=request.user)
    form= expenssForm()

    if request.method == 'POST':
        form = expenssForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            form.save()
        return redirect('/')

    context={'expensess':expensess,
             'form':form}
    return render(request,'walets/walet.html',context)