<h1>Data Represntation & Querying Project Year 3 Semester 1 GMIT</h1>
<br> 
<h2>Post It App</h2>
<br>
This repository contains code and information for a third-year undergraduate project for the module Data Representation and Querying 
That I am currently undertaking
<br>
<h4><b>Project Overview</b></h4> 
I have decided to create a Single-Page Web Application (SPA) that is a simulation of a POST It.

The project was guided by the following excerpt from the project instructions:

You are required to develop a single-page web application(SPA) written in the programming language Python using the Flask framework.

You must devise an idea for a web application, 

write the software, 

write documentation explaining how the application works, and write a short user guide for it.

The application is written using the Flask,Python 3,django as well as rethinkdb 
<br>
ALL must be installed to run the project there is no need to create the database  as the Database will be generated once the application is run.
<br>
if you are still having problems installing these programs

<h4><b>How to run the application</b></h4>
<b>The following requirements are needed before you can run the application</b>
<br>1.download/install python3.5 or above
<br>2.install pip installer
<br>3.install flask and flask-wtf via pip command
<br>4.download and install Rethinkdb from the below link on your prefered OS
<br>

Download links for flask python 3 and rethinkdb see below:

<br>link-->https://www.python.org/downloads/ 
<br>link-->http://flask.pocoo.org/
<br>link-->https://www.djangoproject.com/download/
<br>link-->https://rethinkdb.com/docs/install/

<b>How to install rethink guide for the different OS types</b>
<br>
<br>link-->https://www.rethinkdb.com/docs/install/ubuntu/
<br>link-->https://rethinkdb.com/docs/install/windows/
<br>link-->https://www.rethinkdb.com/docs/install/osx/	   
	   
	   
Then Download a zip version of project and unzip 
<br>
<br>1.open cmd window and cd to the unzipped folder root
<br>2.to run the program you must first start the rethinkdb
<br>3.to do this you must cd into the folder where the rethinkdb.exe file is and run it via command prompt
<br>4.once the database is running it can be accessed by pointing your browser at http://127.0.0.1:8080/
<br>5.to run the app cd to the root of folder of the app in this case Flaskapp
<br>6.type pthon run.py Once the application is running, it can be accessed by pointing your browser at http://127.0.0.1:5000/
<br>7.at http://127.0.0.1:5000/ you will see the main app page
<br>8. you will see a simple post it webapp page simply enter what you want to post into the textbox and click the add it button on screen
<br>9.once the button is clicked the data will be inserted into the database and outputted in a bulletpoint below on the screen 
<br>10.once on this page you can click the Info Icon to get redirected to the about app page which will tell explain about my app as well as a Github link to my code 

<b>Architecture</b>

This web application runs in Python 3 using the Flask web micro-framework,danjgo and  Rethinkdb as a database. 

Python 3 and Flask were requirements for the project But django & Rethinkdb were my choices as  in rethinkdb its a very useful and user friendly database server
to work with once it is setup % django is useful for its template extending  services  

<b>About App</b>

<p><i>The App that I chose to create using (python flask and rethinkdb) is a simple POST IT App. 
The reason I chose this type App was it was relatively not to complex to implement and was something I had been thinking of doing on a different programming language in my spare time.
My Choice of DB was rethinkdb as it is very simplistic to implemnt and scale as well as that it has a very good API libary and documentation on its website 
it is also an opensource database for realtime web apps and is useable on Most Operating Systems available</i></p>

<b>References</b>
I acid stripped a website template from w3schools for the nav bar and the header file --> <br>http://www.w3schools.com/w3css/tryw3css_templates_start_page.htm#
<br>I found the info,github and home buttons logos on this website here -->http://fontawesome.io/icons/#web-application 
