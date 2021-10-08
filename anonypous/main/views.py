from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/dashboard.html', {})


def logout_request(request):
    logout(request)
    return redirect('/')

#will this work i dont know

def root(request):
    return redirect('/login')

def login_request(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        username = username.strip(' ')
        password = password.strip(' ')

        print(f'\nusername = {username}')
        print(f'password = {password}')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user=user)
            print(f'Login Successful\n')
            return redirect('/register/')
        else:
            print("Invalid username or password.\n")


    return render(request, 'dashboard/login.html', context={})

'''
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
                return redirect('/dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'dashboard/login.html', context={"form":form})
'''

def register(request):
    logout(request)
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        account = request.POST.get('account')

        if password == password2:
            print(f"\nusername = {username}")
            print(f"email = {email}")
            print(f"Password = {password}\n")
            print(account)
            print(type(account))
            """
            account = int(account)
            if account == 1:
                print(f"Teacher Account")
            elif account == 0:
                print("Student Account")
            else:
                print('error')
        else:
            print("\npassword did not match\n")
            """

    return render(request, 'dashboard/register.html', context={})

