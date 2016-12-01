# flask g = Just store on this whatever you want. 
#For example a database connection or the user that is currently logged in.
#
#To redirect a user to another endpoint eg a url, use the redirect(url_for(index) function;
#
from flask import render_template, g, url_for, redirect, request ##
from flaskapp import flaskapp
from flaskapp.Myforms import TODOFORM
import json 

# imports
import rethinkdb as myDB
from rethinkdb.errors import RqlRuntimeError, RqlDriverError

# configure Rethink
MY_HOST =  'localhost' #host: the host to connect to (default localhost).
MY_PORT = 28015 	   #port: the port to connect on (default 28015).
MYDATABASE = 'mytable'    #db: the default database (default test).

# db setup;
def dbSetup():
    Database_connection = myDB.connect(host=MY_HOST, port=MY_PORT) #
    try:
        myDB.db_create(MYDATABASE).run(Database_connection)
        myDB.db(MYDATABASE).table_create('mytables').run(Database_connection)
        print('The Database setup has been completed')
    except RqlRuntimeError:
        print('The Database is already Created.')
    finally:
        Database_connection.close()
dbSetup()

# before request open connection
@flaskapp.before_request
def before_request():
    try:
        g.rethinkdb_connection = myDB.connect(host=MY_HOST, port=MY_PORT, db=MYDATABASE) # host ,port and db are all set to preset default values declared above 
    except RqlDriverError:
        abort(503, "Database connection couldn't connect.") 

# after request close the connection
@flaskapp.teardown_request
def teardown_request(exception):
    try:
        g.rethinkdb_connection.close() 
    except AttributeError:
        pass

#index page main page 
@flaskapp.route('/', methods = ['GET', 'POST'])
def index():
        form = TODOFORM() # instansiate form from MyForms.py
        if form.validate_on_submit():  # if form is valid on submit 
                myDB.table('mytables').insert({"name":form.label.data}).run(g.rethinkdb_connection) # insert into mytables form label and run the connection
                return redirect(url_for('index')) # redirect to index.html url  
        MySelection = list(myDB.table('mytables').run(g.rethinkdb_connection)) # list all thats in the database table(mytables) pass the list of strings to my selection variable
        return render_template('index.html', form = form, posts = MySelection)

@flaskapp.route('/about/')
def about():
    return render_template('about.html')