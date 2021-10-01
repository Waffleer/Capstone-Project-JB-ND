from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


from . form import newUserForm, newStudentForm

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/dashboard.html', {})

def logout_request(request):
    logout(request)



def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user=user)
                #messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'dashboard/login.html', context={"form":form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm
        #form = newUserForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user=user)
            return redirect('/profile')

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    form = AuthenticationForm()
    return render(request, 'dashboard/register.html', context={"form":form})


def studentRegister(request):
    if request.method == 'POST':
        form = newStudentForm(request=request, data=request.POST)
        if form.is_valid():

            return redirect('/')

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    form = AuthenticationForm()
    return render(request, 'dashboard/student.html', context={"form":form})

def teacherRegister(request):
    pass

