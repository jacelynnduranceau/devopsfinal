
import os
import exampleDB3 as db
from flask import Flask, request, render_template, jsonify

### main.py
#
## Simple (fat-finger) flask application.  The application acts as a "frontend"
#   for the exampleDB3.py sqlite3 database engine.  
# The container starts by immediately deleting any old versions of the 'eaglesDB.db' SQL database.  If you want to persist
#  this DB then delete these two lines and change the 'createDB' function in exampleDB3.py
#  as appropriate - perhaps reading the DB in from disk first.
#
#    Once it has deleted the old DB, it starts the flask server & listens on 172.17.0.x:5000
# the server continues to spin in background waiting to receive requests from a browser.
#
# After starting the server, flask instantiates the Flask microframework class as 'app' 
# and then waits for flask server to route requests to it, (after the server has received a 
# request from the browser).
#
# This program imports another python module called 'exampleDB3.py' which contains the
# SQLite processing engine.  the python import statement 'import exampleDB3 as db'
# means that any time that we want to call a function in exampleDB3, we need to preface 
# that function call with 'db.'  for example instead of making a call to getPlayers(),
# we need to call db.getPlayers()
#
# This program uses flask to demonstrate how to
#   provide the appropriate URL 'route' from the user - what CRUD operation they
#   would like to perform.  For the sake of time, it only supports the following 
#   routes:
#   '/'      display/send back/render the index.html file (the main welcome page)
#   '/list'  makes a call to exampleDB3.py getPlayers() function that returns a DB dump
#   '/add'   makes a call to exampleDB3.py addPlayer() function to add an entry in the DB
#   '/save'  when user asks to add a player (i.e., we receive an /add route, 'GET' request ),
#            we send them back an html form called 'add.html' to fill in with the 
#            information.  When the user hits 'submit' on the browser, the form returns
#            to us as a 'POST' call from the browser (and is routed to our /save route)
#            this routine then picks apart what the user filled in and calls 'db.addPlayer'
#   '/delete'unimplemented
#
# This program is a slightly more complex version of the testApp.py example and is
# used to demonstrate:
#   docker build process          - multiple python files, HTML files, installing dependencies 
#   containers and SQLite3        - how it's no different than working with non-container based DBMS systems
#   containers and frameworks     - how it's no different than working with non-container frameworks
#   containers and flask and HTML - final image size implications
#  
#  
app = Flask(__name__)                       # instantiate the Flask class

@app.route("/")                             # send the index.html 'welcome' page to the browser
def index():
    return render_template("index.html")    # this file is imbedded in the container

@app.route("/list", methods=["GET"])      # user requested that we list the DB contents
def list():

    conn = db.sqlite3.connect('eaglesDB.db')     # connect to the database
    c = conn.cursor()                            # create the cursor
    c.execute("SELECT * FROM eagles")   # pull everything in the eagles table
    results = c.fetchall()              # put evverything into a list
    c.close()                           # Close the cursor
    conn.close()                        # Shut down the connection to the DB

    return render_template("list.html", results = results)  # send the results back to browser

@app.route("/add")                      # user wants to add a player..... 
def add():                              #    so we need to send the browser a form to fill in the information 
    return render_template("add.html")  #    this form is also embedded in this container

@app.route("/save", methods=["GET", "POST"])
def save():
    if request.method == "POST":
        fName = request.form['fname']
        lName = request.form['lname']
        position = request.form['pos']
        number = request.form['num']
        drafted = request.form['drafted']
        db.addPlayer(fName, lName, position, number, drafted)
        msg = "Player Record Successfully Added "
        return render_template("success.html", msg = msg)

@app.route("/delete")
def delete():

    return render_template("delete.html")



if __name__ == "__main__":
    # print("Directory {} contains: \n".format(os.getcwd()))
    # print(os.listdir(os.getcwd()))
    if os.path.exists('eaglesDB.db'):
        print ("Deleting old versions of eaglesDB.db from the {} directory".format(os.getcwd()))
        os.remove('eaglesDB.db')    # delete any old versions - don't use if you need persistence!

    db.createDB()
    app.run(host='0.0.0.0')    # start up the flask server