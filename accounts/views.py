from django.contrib.auth import login
from django.shortcuts import render, redirect
from accounts.form import SignupForm


# Create your views here.
def signup(request):
    if request.method == "POST":
        print(request.POST)
        form = SignupForm(request.POST)

        print(form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request,'accounts/signup.html',{'form':form})