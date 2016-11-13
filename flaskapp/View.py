from flask import render_template, url_for, redirect, g, request ##
from flaskapp import flaskapp
from flaskapp.Myforms import TODOFORM
import json ##

# rethink imports
import rethinkdb as myDB
from rethinkdb.errors import RqlRuntimeError, RqlDriverError

# rethink config
MY_HOST =  'localhost'
MY_PORT = 28015
MYDATABASE = 'todo'

# db setup; only run once
def dbSetup():
    connection = myDB.connect(host=MY_HOST, port=MY_PORT)
    try:
        myDB.db_create(MYDATABASE).run(connection)
        myDB.db(MYDATABASE).table_create('todos').run(connection)
        print('MYDATABASE setup has been completed')
    except RqlRuntimeError:
        print('The Database already exists.')
    finally:
        connection.close()
dbSetup()

# open connection before each request
@flaskapp.before_request
def before_request():
    try:
        g.rdb_conn = myDB.connect(host=MY_HOST, port=MY_PORT, db=MYDATABASE)
    except RqlDriverError:
        abort(503, "Database connection could be established.")

# close the connection after each request
@flaskapp.teardown_request
def teardown_request(exception):
    try:
        g.rdb_conn.close()
    except AttributeError:
        pass

@flaskapp.route('/', methods = ['GET', 'POST'])
def index():
        form = TODOFORM()
        if form.validate_on_submit(): 
                myDB.table('todos').insert({"name":form.label.data}).run(g.rdb_conn)
                return redirect(url_for('index'))
        MySelection = list(myDB.table('todos').run(g.rdb_conn))
        return render_template('index.html', form = form, tasks = MySelection)