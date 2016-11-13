<h1>TODO Flask-Python App</h1>

<h3><b>Data Representation and Querying GMIT Year3</b></h3>
<br>
This repository contains code and information for a third-year undergraduate project for the module Data Representation and Querying 
That I am currently undertaking
<br>
<h4><b>Project Overview</b></h4> 
I have decided to create a Single-Page Web Application (SPA) that is a simulation of a TODO List.

The project was guided by the following excerpt from the project instructions:

You are required to develop a single-page web application(SPA) written in the programming language Python using the Flask framework.

You must devise an idea for a web application, 

write the software, 

write documentation explaining how the application works, and write a short user guide for it.

<h6>How to run the application</h6>
<br>
<b>The following requirements are needed before you can run the application</b>
1.download/install python3.5 or above
2.install pip installer
3.install flask and flask-wtf via pip command
4.download and install Rethinkdb from the below link on your prefered OS
link-->https://rethinkdb.com/docs/install/

<b>How to install rethink guide for the different OS types</b>
link-->https://www.rethinkdb.com/docs/install/ubuntu/
link-->https://rethinkdb.com/docs/install/windows/
link-->https://www.rethinkdb.com/docs/install/osx/	   
	   
Then Download a zip version of project and unzipp 
open cmd window and cd to the unzipped folder root

to run the app type pthon run.py int the cmd prompt



The application is written using the Flask library in Python 3 as well as rethinkdb 

Both must be installed to run the project there is no need to create the database  as the Database will be generated once the application is run.

<br>
Download links for flask and python 3 see below:
<br> 
https://www.python.org/downloads/ <br>
http://flask.pocoo.org/<br>
<br>
if you are still having problems installing these programs
<br>
I suggest you check out some video tutorials on how to install flask and python
<br>
<br>
I used the sqlite3 package for persistence in the application. This must also be installed. However, no further configuration our setup 
is required, as the database is fully contained in the db directory in this repository.
<br>
Once these prerequisites are installed, the application can be run locally:

<b>python pinterest.py</b> 

Once the application is running, it can be accessed by pointing your browser at http://127.0.0.1:5000/ 

or via clicking on the browser button in pycharm

<b>Architecture</b>

This web application runs in Python 3 using the Flask web micro-framework and uses SQLite as a database. 

Python 3 and Flask were requirements for the project,

SQLite was my choice. 

I chose SQLite as it is easy to use and does not require much setup to get the web application up and running.
