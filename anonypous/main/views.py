
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.models import User
from . models import profile, classes, classcode
import string
import random

def genCode6():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    y = 0
    code = []
    while y < 6:
        num = random.randrange(0, 35)
        code.append(letters[num])
        y += 1
    y = 0
    code = ''.join(code)
    return code

def codecheck(code, codelist):
    if code in codelist:
        codes = classcode.objects.all()
        codelist = []
        for x in codes:
            code = x.code
            codelist.append(code)
        code = genCode6()
        codecheck(code, codelist)
        print('found code')
    else:
        return code



# Create your views here.
def dashboard(request):

    if request.method == 'POST':
        print('\ntest\n')
        print(f'{request.POST}\n')
        if 'cc_className' in request.POST:
            classname = request.POST.get('cc_className')
            color = request.POST.get('classcolor')
            subject = request.POST.get('subject')
            discription = request.POST.get('discription')



            print(f'{classname}\n')
            print(f'{color}\n')
            print(f'{subject}\n')


            codes = classcode.objects.all()
            codelist = []
            for x in codes:
                code = x.code
                codelist.append(code)

            #makes new code
            code = genCode6()
            #checks if code has been used, if not it makes new code and checks again
            code = codecheck(code, codelist)
            code = classcode.objects.create(code=code)





            '''
            name = models.CharField(max_length=30)

            owner = models.OneToOneField(User, on_delete=models.PROTECT, default='')
            discription = models.TextField(default='Description')
            code = models.OneToOneField(classcode, on_delete=CASCADE, default='')

            students = models.ForeignKey(profile, on_delete=PROTECT, default='')
            assignments = models.ForeignKey(assignment, on_delete=PROTECT, default='')

            color = models.IntegerField(default=-1)
            created = models.DateTimeField(auto_now_add=True)
            updated = models.DateTimeField(auto_now=True)
            '''

            currentclass = classes.objects.create(codestr=f'{code}',name=classname, owner=request.user, discription='', code=code, color=color )

            #will deal with the create form post
        elif 'rc_class' in request.POST:

                
            teacherClasses = classes.object.all(owner=request)
            print(teacherClasses)













            print('\nremove \n')
            #will deal with the remove form post
        elif 'jc_classCode' in request.POST:

            currentcode = request.POST.get('jc_classCode')
            currentcode = f'{currentcode}'


            try:
                classs = classes.objects.get(codestr=currentcode)
                print(classs)
                print(type(classs))
                try:
                    classs.students.add(request.user.profile)
                    print(f'Added {request.user} to - {classs.name}')
                    print(classs.students.all())
                except:
                    print("Failed Add to Class - this shouldn't be called")
            except:
                print('class does not exist')

           
            print(f'\njoin') 
            #will deal with the remove form post



    return render(request, 'dashboard/dashboard.html', {})

def submission(request):
    return render(request, 'dashboard/submission.html', {})

def assignment(request):
    return render(request, 'dashboard/assignment.html', {})

def classpage(request):
    return render(request, 'dashboard/class.html', {})

def profiles(request):
    return render(request, 'dashboard/profile.html')

def logout_request(request):
    logout(request)
    return redirect('/')

def root(request):
    return redirect('/login')

def login_request(request):
    context = {
        'authfail' : False,
    }
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')

        username = username.strip(' ')
        password = password.strip(' ')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect('/dashboard')
        else:
            context = {
                'authfail' : True,
            }
            return render(request, 'dashboard/login.html', context)


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
        email2 = request.POST.get('email2')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        account = request.POST.get('account')
        print(account)

        first = first[:29]
        last = last[:29]

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

        if email == email2:
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
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = first
            user.last_name = last
            user.save()
            profile.objects.create(user=user, email=email, teacher=True, firstname=first, lastname=last)
            user = authenticate(username=email, password=password)
            login(request, user=user)
            print(f'Login Successful\n')
            return redirect('/dashboard')
        elif account == 0:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = first
            user.last_name = last
            user.save()
            profile.objects.create(user=user, email=email, teacher=False, firstname=first, lastname=last)
            user = authenticate(username=email, password=password)
            login(request, user=user)
            print(f'Login Successful\n')
            return redirect('/dashboard')

        else:
            print('This shouldnt be triggered')

                

    return render(request, 'dashboard/register.html', context)