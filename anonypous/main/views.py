import smtplib, ssl
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.models import User
from . models import profile, classes, classcode, assignmentcode, assignmentObj, documentcode, doc
import smtplib, ssl
import random
from datetime import datetime

emailBoolean = True

def forms(request):
    return render(request, 'dashboard/forms.html')

def stats(request):
    if request.user.profile.teacher == False:
        return redirect('/invalid')



    classList = classes.objects.filter(ownerstr=request.user)
    print(classList)
    classResults = []

    for x in classList:
        classAdd = []
        classResultSum = 0
        classResultActual = 0
        assignments = x.assignments
        '''
        for y in assignments:
            classResultSum += (y.pointValue * len(assignments))
            submissions = y.submissions
            for z in submissions:
                classResultActual += z.score
        classAdd.append(x.name)
        classAdd.append(classResultActual)
        classAdd.append(classResultSum)
        classResults.append(classAdd)
        '''

    print(classResults)



    return render(request, 'dashboard/stats.html')

def statsAssignment(request, assignmentTag):
    return render(request, 'dashboard/stats.html')

def statsClass(request, classTag):
    return render(request, 'dashboard/stats.html')

def print2(str):
    print(f'\n\n{str}\n\n')

def genCodeClass():
    codelist = []
    codes = classcode.objects.all()
    for x in codes:
        code = x.code
        codelist.append(code)
    code = []
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    y = 0
    while y < 6:
        num = random.randrange(0, len(letters)-1)
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
            num = random.randrange(0, len(letters)-1)
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
            num = random.randrange(0, len(letters)-1)
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

def getClassList(request):
    if request.user.profile.teacher == True:
        #teacher render classes
        classs = classes.objects.filter(ownerstr=request.user)
        classlist = []
        for x in classs:
            currentlist = []
            name = x.name
            subject = x.subject
            code = x.codestr
            currentlist.append(name)
            currentlist.append(code)
            currentlist.append(subject)
            classlist.append(currentlist)
    else:
        #student class render - hella inefficient
        classlist = []
        classs = classes.objects.all()
        for x in classs:
            students = x.students.all()
            for z in students:
                user = str(request.user)
                if user == str(z):
                    print2(f'Worked for class {z}')
                    currentlist = []
                    name = x.name
                    code = x.codestr
                    subject = x.subject
                    currentlist.append(name)
                    currentlist.append(code)
                    currentlist.append(subject)
                    classlist.append(currentlist)
    return classlist

def dashboard(request):
    currentDate = datetime.utcnow()

    if request.user.is_authenticated:
        user = request.user
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
                currentlist.append(subject)
                currentlist.append(color)
                currentlist.append(description)
                classlist.append(currentlist)
                context = {
                'classList': classlist,
                'currentDate': currentDate
                }
        else:
            #student class render - hella inefficient
            classlist = []
            classs = classes.objects.all()
            for x in classs:
                students = x.students.all()
                for z in students:
                    user = str(request.user)
                    if user == str(z):
                        print2(f'Worked for class {z}')
                        currentlist = []
                        name = x.name
                        code = x.codestr
                        color = x.color
                        subject = x.subject
                        description = x.description
                        currentlist.append(name)
                        currentlist.append(code)
                        currentlist.append(subject)
                        currentlist.append(color)
                        currentlist.append(description)
                        classlist.append(currentlist)
            context = {
                'classList': classlist,
                'currentDate': currentDate,
            }
    else:
        return redirect('/login')


    if request.method == 'POST':


        if 'cc_className' in request.POST:
            classname = request.POST.get('cc_className')
            color = request.POST.get('classcolor')
            subject = request.POST.get('subject')
            description = request.POST.get('description')
            year = request.POST.get('year')



            print(f'{classname}\n')
            print(f'{color}\n')
            print(f'{subject}\n')
            print(f'{year}\n')


            codes = classcode.objects.all()
            codelist = []
            for x in codes:
                code = x.code
                codelist.append(code)

            #makes new code
            code = genCodeClass()
            code = classcode.objects.create(code=code)
            currentclass = classes.objects.create(codestr=f'{code}',name=classname, owner=request.user, ownerstr=f'{request.user}', description=description, code=code, color=color, subject=f'{subject}', year=year )
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
                    print2(1)
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
                    'currentDate': currentDate,
                    'classList': classlist,
                }
                print2(2)
                return redirect('/dashboard', context)

           
            print(f'\njoin') 
            #will deal with the remove form post
    try:
        context.update({'null': "null"})
    except:
        context = {}
    return render(request, 'dashboard/dashboard.html', context)

def grade(request, classCode, assignmentCode, docCode):

    
    currentDate = datetime.utcnow()
    if str(docCode) == 'style.css':
        pass
    else:
        try:
            classs = classes.objects.get(codestr=classCode)   
            assignment = assignmentObj.objects.get(codestr=str(assignmentCode))
            document = doc.objects.get(codestr=docCode) 
        except:
            return redirect('/invalid')

        classlist = getClassList(request)
            
        text = str(document.text)
        subDate = document.submissionDate
        docCode = str(document.code)
        feedback = document.comment
        score = document.score


            
        instructions = assignment.instructions
        pointValue = assignment.pointValue
        assignmentOwner = assignment.owner
        submitBool = assignment.submitted

        if assignmentOwner == request.user:

            if request.method == 'POST':

                comments = request.POST.get('feedback')
                score_ = request.POST.get('score')

                
                document.comment = comments
                document.score = score_
                document.save()
                text = str(document.text)
                subDate = document.submissionDate
                docCode = str(document.code)
                feedback = document.comment
                score = document.score
                instructions = assignment.instructions
                pointValue = assignment.pointValue
                assignmentOwner = assignment.owner

                currentDate = datetime.utcnow()
                context = {
                'assignmentText':text,
                'subDate': subDate,
                'docCode': docCode,
                'instructions': instructions,
                'pointValue': pointValue,
                'score': score,
                'feedback': feedback,
                'submitBool': submitBool,
                'currentDate': currentDate,
                'classList': classlist,
                }
                
                return redirect(f'/class/{classCode}/{assignmentCode}')

            context = {
                'assignmentText':text,
                'subDate': subDate,
                'docCode': docCode,
                'instructions': instructions,
                'pointValue': pointValue,
                'score': score,
                'feedback': feedback,
                'submitBool': submitBool,
                'currentDate': currentDate,
                'classList': classlist,

            }


            return render(request, 'dashboard/submission.html', context)
        else:
            return redirect('/invalid')

def results(request, classCode, assignmentCode):
    currentDate = datetime.utcnow()
    user = request.user
    assignment = assignmentObj.objects.get(codestr=str(assignmentCode))
    classs = classes.objects.get(codestr=classCode)    

    submitBool = assignment.submitted
    try:
        classs = classes.objects.get(codestr=classCode)   
        assignment = assignmentObj.objects.get(codestr=str(assignmentCode))
    except:
        return redirect('/invalid')
        
    classlist = getClassList(request)


    if assignment.submitted == True:
        submissions = assignment.submissions.all()
        assignmentName = assignment.name
        pointValue = assignment.pointValue
        submissionList = []
        for x in submissions:
            list = []
            list2 = []
            name = f"{x.owner.profile.firstname} {x.owner.profile.lastname}"
            code = str(x.code)
            code = code.replace('-', ' ')
            score = f"{x.score} / {pointValue}"
            feedback = x.comment
            list.append(x.owner.profile.lastname)
            list.append(x.owner.profile.firstname)
            list.append(name)
            list.append(code)
            list.append(score)
            list.append(feedback)
            submissionList.append(list)

        submissionList = sorted(submissionList)
        for x in submissionList:
            x.pop(0)
            x.pop(0)
        context = {
            'assignmentName': assignmentName,
            'submissions': submissionList,
            'submitBool': submitBool,
            'currentDate': currentDate,
            'classList': classlist,
        }
    else:
        submissions = assignment.submissions.all()
        assignmentName = assignment.name
        pointValue = assignment.pointValue
        submissionList = []
        submitBool = assignment.submitted
        print2(submitBool)
        for x in submissions:
            list = []
            #name = f"{x.owner.profile.firstname} {x.owner.profile.lastname}"
            code = str(x.code)
            code = code.replace('-', ' ')
            score = f"{x.score} / {pointValue}"
            feedback = x.comment
            list.append("")
            list.append(code)
            list.append(score)
            list.append(feedback)
            submissionList.append(list)
        context = {
            'assignmentName': assignmentName,
            'submissions': submissionList,
            'submitBool': submitBool,
            'currentDate': currentDate,
            'classList': classlist,
        }


        if request.method == 'POST':
            if 'submit' in request.POST:
                if emailBoolean == True:
                    
                    print2("kfdsjlkdsflkdfsjkl;dfskljdfsjklfsdlkdfsl;k")
                    #Popup window saying plz wait would be nice
                    assignment = assignmentObj.objects.get(codestr=str(assignmentCode))
                    submissions_ = assignment.submissions.all()

                    reciverList = []
                    nameList = []
                    docInfo = []
                    for x in submissions_:
                        reciverList.append(str(x.owner))
                        nameList.append(str(x.owner.profile.firstname))
                        nameList.append(str(x.owner.profile.lastname))
                        docInfo.append(f"{str(x.score)}/{assignment.pointValue}")
                        docInfo.append(str(x.comment))
                    print(reciverList)
                    print("\n\n")
                    smtp_server = "smtp.gmail.com"
                    port = 587  # For starttls
                    sender = "noreply.anonypous@gmail.com"
                    password = "loginOctopus"
                    context1 = ssl.create_default_context()
                    server = smtplib.SMTP(smtp_server,port)
                    server.starttls(context=context1) # Secure the connection
                    server.login(sender, password)
                    y = 0
                    for x in reciverList:   
                        pass
                        email = f"""
                        From : Anonypous Student Security Site <noreply.anonypous@gmail.com>
                        To : {nameList[y]} {nameList[y+1]} <{x}>
                        Subject: Returning Results on {assignment.name}.

                        Results are :     {docInfo[y]}.
                        Feedback :  
                        {docInfo[y+1]}

                        """
                        server.sendmail(sender, x, email)
                        y += 2
                    server.quit()
                    assignment.submitted = True
                    assignment.save()

                    print2("kfdsjlkdsflkdfsjkl;dfskljdfsjklfsdlkdfsl;k")
                return redirect(f'/class/{classCode}/{assignmentCode}/r/result')
    return render(request, 'dashboard/results.html', context)

def assignment(request, classCode, assignmentCode):
    currentDate = datetime.utcnow()

    classCode = str(classCode)
    #try:
    user = request.user
    if str(assignmentCode) == 'style.css':
        pass
    else:
        try:
            assignment = assignmentObj.objects.get(codestr=str(assignmentCode))
            classs = classes.objects.get(codestr=classCode)   
        except:
            return redirect('/invalid') 

        classlist = getClassList(request)

        user = request.user
        students = classs.students.all()    
        name = assignment.name
        code = assignment.code
        owner = assignment.owner
        instructions = assignment.instructions
        pointValue = assignment.pointValue
        assignmentDueDate = assignment.dueDate
        assignmentSubmitted = assignment.submitted
        if user.profile.teacher == True:
            if str(owner) != str(user):
                return redirect("/invalid")
            assignment = assignmentObj.objects.get(codestr=str(assignmentCode))
            classs = classes.objects.get(codestr=classCode)    
            user = request.user
            students = classs.students.all()    
            name = assignment.name
            code = assignment.code
            owner = assignment.owner
            instructions = assignment.instructions
            pointValue = assignment.pointValue
            assignmentDueDate = assignment.dueDate
            feedback = ''

            #configure submission array
            text = ''
            assignment = assignmentObj.objects.get(codestr=str(assignmentCode))
            sublist = []
            for x in assignment.submissions.all():
                if x.submitted != False:
                    if x.open == False:
                        commit = True
                    submission = []
                    code = x.code
                    text = x.text
                    score = x.score
                    submissionDate = x.submissionDate
                    late = False
                    if x.submissionDate > assignmentDueDate:
                        late = True
                    submission.append(code)
                    submission.append(text)
                    submission.append(submissionDate)
                    submission.append(late)
                    submission.append(score)
                    sublist.append(submission)
                    
                    
            for x in assignment.submissions.all():
                if str(x.owner) == str(user):
                    text = x.text
            context = {
            'classCode': classCode,
                'assignmentName': name,
            'assignmentCode': code,
                'assignmentInstructions': instructions,
            'dueDate': assignmentDueDate,
                'pointValue': pointValue,
            'submissions': sublist,
            'assignmentList': [],
                'text': text,
                'currentDate': currentDate,
                'classList': classlist,
            }
        else:
            feedback = ''
            score = ''
            passed = False
            late = False
            for x in students:
                if str(x) == str(user):
                    passed = True
            if passed == False:
                return redirect("/invalid")
            passed = False
            for x in assignment.submissions.all():
                if str(x.owner) == str(user):
                    text = x.text
                    submitted = x.submitted
                    passed = True
                    score = x.score
                    feedback = x.comment
                    if x.submissionDate > assignmentDueDate:
                        late = True

            if passed == False:
                submitted = False
                text = ''
            
            currentDate = datetime.utcnow()
            context = {
                'assignmentSubmitted': assignmentSubmitted,
                'feedback': feedback,
                'score': score,
                'assignmentName': name,
                'assignmentInstructions': instructions,
                'submitted': submitted,
                'dueDate': assignmentDueDate,
                'pointValue': pointValue,
                'text': text,
                'late': late,
                'currentDate': currentDate,
                'classList': classlist,
            }


        if user.profile.teacher == False:
            #If Student
            if request.method == 'POST':
                assignment = assignmentObj.objects.get(codestr=str(assignmentCode))
                print2(assignment.submitted)
                if assignment.submitted != True:
                    text = request.POST.get('text')
                    currentTime = datetime.now()
                    docName = 'Name TBD'
                    
                    assignmentCreate = True
                    for x in assignment.submissions.all():
                        if str(x.owner) == str(user):
                            assignmentCreate = False
                            x.submissionDate = currentTime
                            x.text = text
                            text = x.text
                            x.save()
                            currentdoc = x
                    code = genCodeDoc()
                    docCode = documentcode.objects.create(code=str(code))
                    date = currentTime
                    if assignmentCreate == True:
                        currentdoc = doc.objects.create(name=str(docName), owner=user, code=docCode, text=text, codestr=str(docCode), submissionDate=date, submitted=False)
                        assignment.submissions.add(currentdoc)
                        user.profile.submissions.add(docCode)
                    context = {
                    'assignmentName': name,
                    'assignmentCode': code,
                    'assignmentInstructions': instructions,
                    'pointValue': pointValue,
                    'text': text,
                    'dueDate': assignmentDueDate,
                    'currentDate': currentDate,
                    'classList': classlist,
                    }
                    
                    if 'resubmit' in request.POST:
                        return redirect(f'/class/{classCode}')
                    if 'submit' in request.POST:
                        currentdoc.submitted = True
                        currentdoc.save()
                        return redirect(f'/class/{classCode}')
                    else:
                        return redirect(f'/class/{classCode}/{assignmentCode}')
        else:
            #If Teacher
            if request.method == 'POST':
                return redirect(f'/class/{classCode}/{assignmentCode}/r/result')

        #except:
        #   print('not a valid class')
            #return render(request, 'dashboard/class.html', context)
        #   return redirect('/invalid')

        return render(request, 'dashboard/assignment.html', context)

def classpage(request, classCode):
    currentDate = datetime.utcnow()
    print(f'code - [{classCode}]')
    classCode = str(classCode)
    #try:

    try:
        classs = classes.objects.get(codestr=classCode)    
    except:
        print2("Failed classs find")
        return redirect('/invalid')

    classlist = getClassList(request)

    name = classs.name
    code = classs.code
    owner = classs.owner
    year = classs.year
    description = classs.description
    studentsList = classs.students.all()
    students = []
    for x in studentsList:
        list = []
        nameS = x.firstname
        nameSL = x.lastname
        emailS = x.email
        list.append(nameS)
        list.append(nameSL)
        list.append(emailS)
        students.append(list)

    rawAssignments = classs.assignments.all()
    
    assignments = []
    for x in rawAssignments:
        assignmentList = []
        assignmentList.append(x.name)
        assignmentList.append(x.dueDate)
        assignmentList.append(x.code)
        print(x.code)
        assignments.append(assignmentList)
    
    currentDate = datetime.utcnow()

    context = {
    'className': name,
    'classCode': code,
    'classDescription': description,
    'students': students,
    'assignments': assignments,
    'assignmentList': [],
    'year': year,
    'currentDate': currentDate,
    'classList': classlist,
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
            x = x[2]
            print(request.user)
            print(x)
            if str(request.user) == str(x):
                return render(request, 'dashboard/class.html', context)
        return redirect('/invalid')














    #except:
     #   print('not a valid class')
        #return render(request, 'dashboard/class.html', context)
     #   return redirect('/invalid')

def profiles(request):
    currentDate = datetime.utcnow()


    classlist = getClassList(request)

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
    currentDate = datetime.utcnow()


    classlist = getClassList(request)


    '''
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender = "noreply.aonoypous@gmail.com"
    password = "loginOctopus"

    receiver = "ndwafflend@gmail.com"
    message = "jflkdsafjdjslkafjdsjafjdksjafjdlsk"

    
    context1 = ssl.create_default_context()
    server = smtplib.SMTP(smtp_server,port)
    server.starttls(context=context1) # Secure the connection
    server.login(sender, password)

    server.sendmail(sender, receiver, message)
    server.quit()
    '''
    context = {
        'currentDate': currentDate,
        'classList': classlist,
    }


    return render(request, 'dashboard/test.html', context)

def login_request(request):

    classlist = []
    classss = classes.objects.all()
    for x in classss:
        students = x.students.all()
        for z in students:
            userStr = str(request.user)
            if userStr == str(z):
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


    currentDate = datetime.utcnow()
    context = {
        'authfail' : False,
        'currentDate': currentDate,
        'classList': classlist,
    }
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')


        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user=user)
            print2(3)
            return redirect('/dashboard')
        else:
            context = {
                'authfail' : True,
                'currentDate': currentDate,
                'classList': classlist,
            }
            return render(request, 'dashboard/login.html', context)


    return render(request, 'dashboard/login.html', context={})

def register(request):
    logout(request)
    currentDate = datetime.utcnow()

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
            'currentDate': currentDate,
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
                'currentDate': currentDate,
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
                'currentDate': currentDate,
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
                'currentDate': currentDate,
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
                'currentDate': currentDate,
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
                'currentDate': currentDate,
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
                'currentDate': currentDate,
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
                'currentDate': currentDate,
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
                'currentDate': currentDate,
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
            print2(4)
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
            print2(5)
            return redirect('/dashboard')

        else:
            print('This shouldnt be triggered')

                

    return render(request, 'dashboard/register.html', context)


