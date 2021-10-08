
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.models import User
from . models import profile

# Create your views here.
def dashboard(request):

    if request.method == 'POST':
        if 'create_class' in request.POST:
            pass
            #will deal with the create form post
        elif 'remove_class' in request.POST:
            pass
            #will deal with the remove form post
        elif 'join_class' in request.POST:
            pass
            #will deal with the remove form post



    return render(request, 'dashboard/dashboard.html', {})

def profiles(request):
    return render(request, 'dashboard/profile.html')


def logout_request(request):
    logout(request)
    return redirect('/')


def root(request):
    return redirect('/login')

def login_request(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')

        username = username.strip(' ')
        password = password.strip(' ')

        print(f'\nusername = {username}')
        print(f'password = {password}')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user=user)
            print(f'Login Successful\n')
            return redirect('/dashboard')
        else:
            print("Invalid username or password.\n")


    return render(request, 'dashboard/login.html', context={})

def register(request):
    logout(request)

    #gets a list of all register emails
    email = profile.objects.all()
    emaillist = []
    for email in email:
        email = email.email
        emaillist.append(email)

  

    '''     This code is useless because we are not useing usernames
    #changes list of users into userlist[]
    User = get_user_model()
    users = User.objects.all()
    users = f'{users}'
    users = users.strip('<QuerySet >')
    users = users.strip('[]')
    users = users.replace('<','')
    users = users.replace('>','')
    userlist_ = users.split(',')
    userlist = []
    for x in userlist_:
        x = x.replace(' ','')
        split = x.split(':')
        current = split[1]
        userlist.append(current)
    '''

    context = {
            'error' : False,
            'error1' : False,
            'error2' : False,
            'error3' : False,
            'error4' : False,
            'error5' : False,
            'error6' : False,
            'error7' : False,
        }
    if request.method == "POST":

        first = request.POST.get('first')
        last = request.POST.get('last')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        account = request.POST.get('account')
        print(account)

        #Password match check
        if password == password2:
            pass
        else:
            print('\n\n')
            print(password)
            print(password2)
            print('Fail')
            print('\n\n')
            context = {
                'error' : True,
                'error1' : True,
                'error2' : False,
                'error3' : False,
                'error4' : False,
                'error5' : False,
                'error6' : False,
                'error7' : False,
                }
            return render(request, 'dashboard/register.html', context)\

        
        numbool = False
        upperbool = False
        length = len(password)
        #password lenght check
        if length < 8:
            context = {
                'error' : True,
                'error1' : False,
                'error2' : False,
                'error3' : False,
                'error4' : False,
                'error5' : False,
                'error6' : True,
                'error7' : False,
                }
            return render(request, 'dashboard/register.html', context)

        #Number and Capital letter check
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for x in password:
            if x in numbers:
                numbool = True
            if x.isupper() == True:
                upperbool = True

        if numbool == True:
            pass
        else:
            context = {
                'error' : True,
                'error1' : False,
                'error2' : False,
                'error3' : False,
                'error4' : True,
                'error5' : False,
                'error6' : False,
                'error7' : False,
                }
            return render(request, 'dashboard/register.html', context)
        if upperbool == True:
            pass
        else:
            context = {
                'error' : True,
                'error1' : False,
                'error2' : False,
                'error3' : False,
                'error4' : False,
                'error5' : True,
                'error6' : False,
                'error7' : False,
                }
            return render(request, 'dashboard/register.html', context)


        #Checks Email Validity
        if '@' in email and '.' in email:
            pass
        else:
            context = {
                'error' : True,
                'error1' : False,
                'error2' : True,
                'error3' : False,
                'error4' : False,
                'error5' : False,
                'error6' : False,
                'error7' : False,
            }
            return render(request, 'dashboard/register.html', context)

        #Checks for matching email
        if email in emaillist:
            context = {
                'error' : True,
                'error1' : False,
                'error2' : False,
                'error3' : False,
                'error4' : False,
                'error5' : False,
                'error6' : False,
                'error7' : True,
                } 
            return render(request, 'dashboard/register.html', context)

        #See if there was a account input

        try:
            account = account.strip(" ")
            account = int(account)
            print('valid')
        except:
            print('failed')
            context = {
                'error' : True,
                'error1' : False,
                'error2' : False,
                'error4' : False,
                'error5' : False,
                'error6' : False,
                'error7' : False,
                } 
            return render(request, 'dashboard/register.html', context)

        #Checks what account type it is
        if account == 1:
            print('1')
            user = User.objects.create_user(username=email, password=password)
            profile.objects.create(user=user, email=email, teacher=True, firstname=first, lastname=last)
            return redirect('/dashboard')
        elif account == 0:
            print('1')
            user = User.objects.create_user(username=email, password=password)
            profile.objects.create(user=user, email=email, teacher=False, firstname=first, lastname=last)
            return redirect('/dashboard')

        else:
            print('This shouldnt be triggered')

                

    return render(request, 'dashboard/register.html', context)