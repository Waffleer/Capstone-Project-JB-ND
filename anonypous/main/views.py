
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.models import User
from . models import profile, classes, classcode, assignmentcode, assignmentObj, documentcode, doc

import random
from datetime import datetime

def print2(str):
    print(f'\n\n{str}\n\n')

def genCodeClass():
    codelist = []
    codes = classcode.objects.all()
    for x in codes:
        code = x.code
        codelist.append(code)
    code = []
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    y = 0
    while y < 6:
        num = random.randrange(0, 35)
        code.append(letters[num])
        y += 1
    y = 0
    code = ''.join(code)
    print(code)
    print(codelist)
    for x in codelist:
        if code == x:
            print('Code already used')
            genCodeClass()
    return code

def genCodeAssignment():

    codelist = []
    codes = assignmentcode.objects.all()
    for x in codes:
        code = x.code
        codelist.append(code)
    code = []
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    y = 0
    while y < 17:
        if y == 5 or y == 11:
            code.append('-')
        else:
            num = random.randrange(0, 35)
            code.append(letters[num])
        y += 1
    y = 0
    code = ''.join(code)
    print(code)
    print(codelist)
    for x in codelist:
        if code == x:
            print('Code already used')
            genCodeAssignment()
    return code

def genCodeDoc():
    codelist = []
    codes = documentcode.objects.all()
    for x in codes:
        code = x.code
        codelist.append(code)
    code = []
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    y = 0
    while y < 23:
        if y == 5 or y == 11 or y == 17:
            code.append('-')
        else:
            num = random.randrange(0, 35)
            code.append(letters[num])
        y += 1
    y = 0
    code = ''.join(code)
    for x in codelist:
        if code == x:
            genCodeDoc()
    return code

def invalid(request):
    return render(request, 'dashboard/invalid.html')

# Create your views here.
def dashboard(request):
    context = {
        'classFail': False,
    }
    user = request.user
    if request.user.is_authenticated:
        if user.profile.teacher == True:
            #teacher render classes
            classs = classes.objects.filter(ownerstr=user)
            classlist = []
            for x in classs:
                currentlist = []
                name = x.name
                code = x.codestr
                color = x.color
                subject = x.subject
                description = x.description
                currentlist.append(name)
                currentlist.append(code)
                currentlist.append(color)
                currentlist.append(subject)
                currentlist.append(description)
                classlist.append(currentlist)
                context = {
                'classList': classlist,
                }
        else:
            #student class render - hella inefficient
            classlist = []
            classs = classes.objects.all()
            for x in classs:
                students = x.students.all()
                for z in students:
                    c = str(z)
                    user = str(request.user)
                    if user == c:
                        print2(f'Worked for class {c}')
                        currentlist = []
                        name = x.name
                        code = x.codestr
                        color = x.color
                        subject = x.subject
                        description = x.description
                        currentlist.append(name)
                        currentlist.append(code)
                        currentlist.append(color)
                        currentlist.append(subject)
                        currentlist.append(description)
                        classlist.append(currentlist)




            print2(classs)
            context = {
                'classList': classlist,
            }
    else:
        return redirect('/login')

    if request.method == 'POST':
        print('\ntest\n')
        print(f'{request.POST}\n')
        #rendering stuff

        if 'cc_className' in request.POST:
            classname = request.POST.get('cc_className')
            color = request.POST.get('classcolor')
            subject = request.POST.get('subject')
            description = request.POST.get('description')



            print(f'{classname}\n')
            print(f'{color}\n')
            print(f'{subject}\n')


            codes = classcode.objects.all()
            codelist = []
            for x in codes:
                code = x.code
                codelist.append(code)

            #makes new code
            code = genCodeClass()
            code = classcode.objects.create(code=code)
            currentclass = classes.objects.create(codestr=f'{code}',name=classname, owner=request.user, ownerstr=f'{request.user}', description=description, code=code, color=color, subject=f'{subject}' )
            return redirect(f'class/{code}/')
            #will deal with the create form post
        elif 'rc_class' in request.POST:

            
            classs = classes.objects.filter(ownerstr=user)
            for x in classs:
                print2('woked')
                print(x)
                print(str(request.POST.get('rc_class')))
                c = str(x)
                
                if str(request.POST.get('rc_class')) == c:
                    print2(f' = {x}')
                    x.delete()
                    return redirect('/dashboard')

                

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
                    classs.save()
                    return redirect(f'class/{currentcode}/')
                except:
                    print("Failed Add to Class - this shouldn't be called")


            except:
                print('class does not exist')
                context = {
                    'classFail': True,
                }
                return redirect('/dashboard', context)

           
            print(f'\njoin') 
            #will deal with the remove form post


    return render(request, 'dashboard/dashboard.html', context)

def grade(request, classCode, assignmentCode, docCode):



    context = {}
    return render(request, 'dashboard/submission.html', context)

def assignment(request, classCode, assignmentCode):
    context = {}

    print(f'code - [{classCode}]')
    classCode = str(classCode)
    #try:

    if str(assignmentCode) == 'style.css':
        pass
    else:
        assignment = assignmentObj.objects.get(codestr=str(assignmentCode))
        classs = classes.objects.get(codestr=classCode)    
        user = request.user
        students = classs.students.all()    

        name = assignment.name
        code = assignment.code
        owner = assignment.owner
        instructions = assignment.instructions
        pointValue = assignment.pointValue
        submissions = assignment.submissions.all()

        #configure submission array
        text = ''
        assignment = assignmentObj.objects.get(codestr=str(assignmentCode))
        sublist = []
        for x in assignment.submissions.all():
            submission = []
            code = x.code
            text = x.text
            submissionDate = x.submissionDate
            submission.append(code)
            submission.append(text)
            submission.append(submissionDate)
            sublist.append(submission)

        for x in assignment.submissions.all():
            if str(x.owner) == str(user):
                text = x.text





        context = {
        'classCode': classCode,
        'assignmentName': name,
        'assignmentCode': code,
        'assignmentInstructions': instructions,
        'pointValue': pointValue,
        'submissions': sublist,
        'assignmentList': [],
        'text': text,

        }
        
        
        if request.method == 'POST':
            text = request.POST.get('text')


            currentTime = datetime.now()
            

            assignment = assignmentObj.objects.get(codestr=str(assignmentCode))
            docName = 'Name TBD'
            
            assignmentCreate = True
            for x in assignment.submissions.all():
                if str(x.owner) == str(user):
                    assignmentCreate = False
                    x.submissionDate = currentTime
                    x.text = text
                    text = x.text
                    x.save()
            code = genCodeDoc()
            docCode = documentcode.objects.create(code=str(code))
            if assignmentCreate == True:
                currentdoc = doc.objects.create(name=str(docName), owner=user, code=docCode, text=text)
                assignment.submissions.add(currentdoc)
                user.profile.submissions.add(docCode)

            

            context = {
            'assignmentName': name,
            'assignmentCode': code,
            'assignmentInstructions': instructions,
            'pointValue': pointValue,
            'submissions': submissions,
            'assignmentList': [],
            'text': text
            }

            return render(request, 'dashboard/assignment.html', context)


                
        if str(request.user) == assignment.ownerstr:
            return render(request, 'dashboard/assignment.html', context)
    
        else:
            for x in students:
                x = str(x)
                if str(request.user) == x:
                    return render(request, 'dashboard/assignment.html', context)
            return redirect('/invalid')



        #except:
        #   print('not a valid class')
            #return render(request, 'dashboard/class.html', context)
        #   return redirect('/invalid')

    return render(request, 'dashboard/assignment.html', context)

def classpage(request, classCode):

    print(f'code - [{classCode}]')
    classCode = str(classCode)
    #try:


    classs = classes.objects.get(codestr=classCode)    

    name = classs.name
    code = classs.code
    owner = classs.owner
    description = classs.description
    students = classs.students.all()
    rawAssignments = classs.assignments.all()
    print('\n\n')
    print(f'name-{name}')
    print(f'code-{code}')
    print(f'owner-{owner}')
    print(f'description-{description}')
    print(f'students-{students}')
    print(f'assignments-{rawAssignments}')
    print('\n\n')
    
    assignments = []
    for x in rawAssignments:
        assignmentList = []
        assignmentList.append(x.name)
        assignmentList.append(x.dueDate)
        assignmentList.append(x.code)
        print(x.code)
        assignments.append(assignmentList)

    context = {
    'className': name,
    'classCode': code,
    'classDescription': description,
    'students': students,
    'assignments': assignments,
    'assignmentList': []
    }
    currentClass = code

    if request.method == 'POST':
            print('\ntest\n')
            print(f'{request.POST}\n')
            #rendering stuff
            user = request.user

            #Finished
            if 'cc_assignmentName' in request.POST:
                print2('dfjkdfkjfdskjsdfkljsdfkjlfsdkjjkfs')
                assignmentname = request.POST.get('cc_assignmentName')
                pointValue = request.POST.get('pointValue')
                dueDate = request.POST.get('dueDate')
                instructions = request.POST.get('instructions')



                code = genCodeAssignment()
                code = assignmentcode.objects.create(code=code)
                code.save()
                print(f'\n\n{assignmentname}')
                print(pointValue)
                print(dueDate)
                print(instructions)
                print(f'{code}\n\n')


                print(1)
                user = request.user
                print(2)
                currentAssignment = assignmentObj.objects.create(name=str(assignmentname), owner=user, ownerstr=str(user), code=code, codestr=str(code), pointValue=int(pointValue), instructions=str(instructions), dueDate=dueDate)
                print('jkdsajklfdljsafjlksdlkfslsgefefkldsfjkldjsl;fjdlk;sa')
                print(currentClass)
                print(code)
                currentAssignment.save()

                classs.assignments.add(currentAssignment)
                print('added class')
                print(classs.assignments.all())
                return redirect(f'{str(code)}/')

            #To Do
            elif 'ra_class' in request.POST:
                
                assignments = assignmentObj.objects.filter(ownerstr=user)
                for x in assignments:
                    c = x.code
                    c = str(c)
                    if str(request.POST.get('ra_class')) == c:
                        print2(f'Deleted = {x.name}')
                        x.delete()
                        return redirect(f'/class/{classCode}/')

                    

                #will deal with the remove form post    

    if str(request.user) == classs.ownerstr:
        return render(request, 'dashboard/class.html', context)
 
    else:
        for x in students:
            print2(x)
            print(request.user)
            x = str(x)
            if str(request.user) == x:
                return render(request, 'dashboard/class.html', context)
        return redirect('/invalid')














    #except:
     #   print('not a valid class')
        #return render(request, 'dashboard/class.html', context)
     #   return redirect('/invalid')

def profiles(request):

    if request.method == "POST":
        print('hsagjklgs')
        first = request.POST.get('firstName')
        last = request.POST.get('lastName')
        email = request.POST.get('email')

        user = request.user
        
        user.profile.firstname = first
        user.profile.lastname = last
        user.profile.email = email
        user.profile.save()


    return render(request, 'dashboard/profile.html')

def logout_request(request):
    logout(request)
    return redirect('/')

def root(request):
    return redirect('/login')

def test(request):
    context = {
    }

    return render(request, 'dashboard/test.html', context)

def login_request(request):
    context = {
        'authfail' : False,
    }
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')


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