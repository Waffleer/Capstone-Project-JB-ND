# Capstone Project JB-ND

# How to set up:

Download and install a copy of python 3.9 (https://www.python.org/downloads/release/python-399/)

Make sure to add python to your path, this is a non default option in the installer

Once you are done you, you need to add django using pip, the python package installer

 
pip install django

or 

pip3 install django

for windows if pip does not work, use
py -m pip install django



if there are any errors running the code that has a missing library error, you will likely have to use pip to install that package

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
  
