# Capstone Project JB-ND

# Project Overview
While teachers undoubtedly always try their best to grade each and every one of their students fairly, circumstances can arise where teachers inadvertently utilize bias in their grading at the expense of the student. Not only does the existence of a potential for bias cause educators to doubt their own methods, but it also allows for a certain level of distrust between students and teachers, which is ultimately not healthy. Furthermore, when students receive a poor marking on an assignment they almost always blame the educator for using bias in their grading rather than learning from their errors. This ultimately stunts valuable learning and nullifies constructive feedback. While grading bias may seem, and, in many cases, be, rare, the mere opportunity for it can both allow it to happen unnoticed and/or force students to second guess their grade and ultimately their teacher. By eliminating the possibility of bias, we are giving students the opportunity to have raw, unfiltered grades and feedback that can help them grow in their learning and we are giving teachers the opportunity to be confident in their grading and know that they are giving their students feedback they can value and trust. To make this happen, we had to find a solution that was both practical by today’s educational standards and effective in preventing the opportunity for bias. Due to the recent influence of technology in education, we felt it was fitting to create a web app similar to other educational suites that could foster our solution. We needed to make sure the app was easy to use for both the teacher and the student, so we tried not to make any confusing processes or too many pages or elements. Finally, we needed to come up with our process from the time the assignment was posted to the time it was graded. For this, we simply assigned a random code for each submission a student entered when submitting their work. This way, the teacher can only see the contents of a submission but not the name of the person who submitted it. The teacher can then grade submissions as they come in and write feedback over time. Teachers can save their work and come back later if they would like. Once all submissions are graded, teachers can confirm their grades and commit. Once the teacher commits, they are redirected to a new page that now shows the name of each student and what their score and feedback was in alphabetical order for gradebook entry. At this point, we were concerned that, in an unlikely event, bias could be implemented at the last minute and a teacher could alter a grade for a student between the time that they commit to the grades on our app and the time that they enter the grades into their school’s gradebook software. To prevent the opportunity for bias at this step, we implemented a process to email each student with their scores and feedback at the time that the teacher commits, so that students have the opportunity to see grades and feedback that were given before the teacher had the opportunity to associate the names of the students with the assignment. This way, if there is a variation between what the teacher marked in our app and what is reflected in the school’s gradebook software, the student will know. After vigorous testing, we are happy to report that our app functions in every way that we have intended it to and is ready for use in any classroom once we deploy it publicly. Our solution is unique because its sole focus is anonymity and blind grading. While other educational softwares offer blind grading, most give teachers the option to toggle anonymity on and off. We do not have that option, therefore we give true and full anonymity with every assignment posted on our app.



# Design Choices
Website - We believe that a website fits well with other educational software currently available to teachers making our product more accessible and simple.
Django - The three main options we had for back-end website code to get our project to where we needed it to be was Javascript, PHP, and Python (with Django). We felt that Javascript would not be quite powerful or secure enough to run our site. We also had very limited knowledge of PHP and that, combined with its complexity and old age, we decided it was not a proper solution. Finally we chose Django because it uses Python, which we are both very familiar with, and came with built in libraries for login, profile, and other features necessary for our project.
TinyMCE (Rich text editor) - We knew that we wanted a rich text editor so that students could create work in our application that looks just as if it was created in any word processing software or paste in work from a word processing software and keep all of its original formatting. TinyMCE was an obvious choice because it is a free and open source solution that allows us to completely customize our text boxes and offer more functions such as saving and printing.


# Final Reflection
We feel that our project exceeded our expectations in many ways with our basic criteria. Our project successfully provides teachers with a list of student submitted assignments that can be graded anonymously without the teacher knowing which assignment was turned in by which student. This tells us that we have successfully met our criteria of true anonymity. We also wanted to make our website easy to use, and we feel that we accomplished that by making in-page popups to minimize redirections and make the process very simple and straightforward for both the teacher and the student. We do feel we could improve on the ease of use, however, by offering LMS/SIS integrations and creating a new user tutorial. Given the nature of our project, we felt it was also crucial to make sure our site was secure, and we believe we accomplished that by using Django’s native authentication system tied into our website. We, in the future, would like to add Google and Microsoft authentication both for security and practicality. In addition to these criteria, we also wanted to be able to group students in classes rather than have them floating around where teachers have to do more jumping around to get all of the assignments graded. To do this, we were able to allow teachers to create a class and allow students to join the class with a unique code and be associated with that class in our databases. We feel that we accomplished that perfectly. Another criteria we had was to be able to return the grade to the students so they would see the anonymous grade before it was put into the official gradebook. To do this, we created a script to send each student an email with their score and feedback. While this is functional when running off of our server, it has run into a few bugs and we would like to streamline that in the future and possibly allow for students to see their grade natively on the app as well. Finally, we wanted to allow teachers to be able to give feedback, which we were able to do by adding a large text box so teachers could write feedback specific to each assignment that the student can see and use to improve. This feedback is sent along with scores in the email to the student and reflected on the results page for the teacher to enter into the gradebook for notes. While we could see a few future improvements such as login authentication, LMS/SIS integration, and email fine-tuning, we feel that overall our project both met and exceeded our initial expectations and performs each of its tasks well.

# Website Demo  By Jake Busse


# Website Structure
![Jake Busse   Nick Doboszenski- E3 Presentation - Final (23)](https://github.com/Waffleer/Capstone-Project-JB-ND/assets/84477153/d6bf29d7-4dec-470d-a5d5-69d5d2aa4155)
![Jake Busse   Nick Doboszenski- E3 Presentation - Final (21)](https://github.com/Waffleer/Capstone-Project-JB-ND/assets/84477153/6319816e-744c-48fd-a6d0-88613c0214ef)
![Jake Busse   Nick Doboszenski- E3 Presentation - Final (22)](https://github.com/Waffleer/Capstone-Project-JB-ND/assets/84477153/8f04bc67-1f74-4660-8232-a25fbe711a9b)


# Images of Website
![Jake Busse   Nick Doboszenski- E3 Presentation - Final](https://github.com/Waffleer/Capstone-Project-JB-ND/assets/84477153/0a923902-9025-4a73-8b12-bc6bd95eeb13)
![Jake Busse   Nick Doboszenski- E3 Presentation - Final (1)](https://github.com/Waffleer/Capstone-Project-JB-ND/assets/84477153/29013262-21d4-4804-bfec-fb47f6f415b8)
![Jake Busse   Nick Doboszenski- E3 Presentation - Final (2)](https://github.com/Waffleer/Capstone-Project-JB-ND/assets/84477153/5fdfe883-e0a4-48e8-8fce-0d73952ec4e0)
![Jake Busse   Nick Doboszenski- E3 Presentation - Final (3)](https://github.com/Waffleer/Capstone-Project-JB-ND/assets/84477153/6a81262e-fea1-4545-9b6b-7718d5bf5539)
![Jake Busse   Nick Doboszenski- E3 Presentation - Final (4)](https://github.com/Waffleer/Capstone-Project-JB-ND/assets/84477153/280da9f4-ec2d-4252-b868-7ec3fbc375fd)
![Jake Busse   Nick Doboszenski- E3 Presentation - Final (5)](https://github.com/Waffleer/Capstone-Project-JB-ND/assets/84477153/15814b4c-d744-4b7e-825e-0f13a5e063bb)
![Jake Busse   Nick Doboszenski- E3 Presentation - Final (6)](https://github.com/Waffleer/Capstone-Project-JB-ND/assets/84477153/19743815-2482-4e1f-98ea-e0d4b5e644d2)
![Jake Busse   Nick Doboszenski- E3 Presentation - Final (7)](https://github.com/Waffleer/Capstone-Project-JB-ND/assets/84477153/ef80663e-ffe7-4a7c-b8f9-7a2af86839d8)
![Jake Busse   Nick Doboszenski- E3 Presentation - Final (8)](https://github.com/Waffleer/Capstone-Project-JB-ND/assets/84477153/049ff7cf-fcd7-481e-a974-2615124068ad)
![Jake Busse   Nick Doboszenski- E3 Presentation - Final (9)](https://github.com/Waffleer/Capstone-Project-JB-ND/assets/84477153/ecf9dbdf-dffd-495e-94e5-b05de871a358)
![Jake Busse   Nick Doboszenski- E3 Presentation - Final (10)](https://github.com/Waffleer/Capstone-Project-JB-ND/assets/84477153/0f3469cd-5d09-4fd1-ac36-c62d98fbbcf4)
![Jake Busse   Nick Doboszenski- E3 Presentation - Final (11)](https://github.com/Waffleer/Capstone-Project-JB-ND/assets/84477153/751e6daa-9036-4eee-baaf-f473e17e68e7)
![Jake Busse   Nick Doboszenski- E3 Presentation - Final (12)](https://github.com/Waffleer/Capstone-Project-JB-ND/assets/84477153/aa373c9e-ff31-421a-9c0c-ec93319847c9)
![Jake Busse   Nick Doboszenski- E3 Presentation - Final (13)](https://github.com/Waffleer/Capstone-Project-JB-ND/assets/84477153/5f6b758a-93e8-43d8-a918-7ac19831bf1a)
![Jake Busse   Nick Doboszenski- E3 Presentation - Final (14)](https://github.com/Waffleer/Capstone-Project-JB-ND/assets/84477153/cb796fea-5dd3-48ea-babb-dc84af2e9f7b)
![Jake Busse   Nick Doboszenski- E3 Presentation - Final (15)](https://github.com/Waffleer/Capstone-Project-JB-ND/assets/84477153/882e65f6-3658-4efb-b1f0-3c309fff4dd6)
![Jake Busse   Nick Doboszenski- E3 Presentation - Final (16)](https://github.com/Waffleer/Capstone-Project-JB-ND/assets/84477153/52e57ce1-08c9-41f6-b626-45388d097c56)
![Jake Busse   Nick Doboszenski- E3 Presentation - Final (17)](https://github.com/Waffleer/Capstone-Project-JB-ND/assets/84477153/982f723e-ece5-4b71-b4bc-795b4acdd65e)
![Jake Busse   Nick Doboszenski- E3 Presentation - Final (18)](https://github.com/Waffleer/Capstone-Project-JB-ND/assets/84477153/097aa361-58d4-454e-ad0e-1bf48dad54ec)



# How to set up:

Download and install a copy of python 3.9 (https://www.python.org/downloads/release/python-399/)

Make sure to add python to your path, this is a non default option in the installer

Once you are done you, you need to add django using pip, the python package installer

 
pip install django

or 

pip3 install django

for windows if pip does not work, use
py -m pip install django



if there are any missing library errors, you will likely have to use pip to install that package
  Please tell me if any exist and I will update the list

Download the zip of this repository and extract it somewhere on on your computer.

Open up terminal and cd to the folder

cd moves the directory the terminal is running from
you can user dir or ls depending on your os to see all of the files in that directory
if you are not running terminal as admin then you will start in your user folder,
example :
  cd /Desktop/Capstone-Project-JB-ND
  
  
then cd to the anonypous folder
 cd /anonypous
 
 if you run dir or ls you should see the file "manage.py"
 
 if you don't see the file "manage.py" then you are in the wrong folder.
 
 Once you get into the folder, run 
    python3 manage.py runserver
  
 this will start a development server on your computer, it will show a ip which you can open in your browser
 
 You can also set the development server to your local ip which allows other devices on your wifi access to the website by going to that ip
 example
   python3 manage.py runserver 172.16.0.11:8000
   
   
 If you need any help, feel free to email me
  
 # Known Bugs
 
 If you go to results page in teacher side of website and get a ssl certificate error, this is due to the email ssl not matching with the computer we set it up for. You can fix this bug by going to anonypous/main/view.py and making the variable emailBoolean = False. This will disable the emailing of students fixing the bug. DO NOT PUT THIS AS FALSE IN MAIN BRANCH
  
