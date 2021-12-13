
import os
import exampleDB3 as db
import pokemon as poke
from random import randint
from flask import Flask, request, render_template, redirect, url_for, jsonify

## main.py
#
## Simple (fat-finger) flask application.  The application acts as a "frontend"
#   for the exampleDB3.py sqlite3 database engine.  
# The container starts by immediately deleting any old versions of the 'pokeDB.db' SQL database.  If you want to persist
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
# that function call with 'db.'  for example instead of making a call to getPokemon(),
# we need to call db.getPokemon()
#
# This program uses flask to demonstrate how to
#   provide the appropriate URL 'route' from the user - what CRUD operation they
#   would like to perform.  For the sake of time, it only supports the following 
#   routes:
#   '/'      display/send back/render the index.html file (the main welcome page)
#   '/pokedex'  makes a call to exampleDB3.py getPokemon() function that returns a DB dump
#   '/catch'   makes a call to exampleDB3.py addPokemon() function to add an entry in the DB
#   '/save'  when user asks to catch a pokemon (i.e., we receive an /catch route, 'GET' request ),
#            we send them back an html form called 'catch.html' to fill in with the 
#            information.  When the user hits 'submit' on the browser, the form returns
#            to us as a 'POST' call from the browser (and is routed to our /save route)
#            this routine then picks apart what the user filled in and calls 'db.addPokemon'
#   '/delete_pokemon' deletes a pokemon from the database / pokedex

app = Flask(__name__)                       # instantiate the Flask class

@app.route("/")                             # send the index.html 'welcome' page to the browser
def index():
    return render_template("index.html")    # this file is imbedded in the container

@app.route("/pokedex", methods=["GET"])      # user requested that we list the DB contents via the pokedex
def pokedex():
    conn = db.sqlite3.connect('pokeDB.db')     # connect to the database
    c = conn.cursor()                            # create the cursor
    c.execute("SELECT * FROM pokemon")   # pull everything in the pokemon table
    results = c.fetchall()              # put evverything into a list
    c.close()                           # Close the cursor
    conn.close()                        # Shut down the connection to the DB
    return render_template("pokedex.html", results = results)  # send the results back to browser

@app.route("/delete_pokemon", methods=["POST"]) 
def delete_pokemon():
    id = request.form['id']
    db.deletePokemon(str(id))
    return redirect(url_for('pokedex'))  # send the results back to browser

@app.route("/catch", methods=["GET"])      # user wants to catch a pokemon..... 
def catch():   
    pokemon = generate_random_pokemon()
    results = []
    results.append(pokemon.image_png)
    results.append(pokemon.number)
    results.append(pokemon.name)
    results.append(pokemon.height)
    results.append(pokemon.weight)
    results.append(pokemon.type1)
    results.append(pokemon.type2)
    results.append(pokemon.ability1)
    results.append(pokemon.ability2)
    return render_template("catch.html", results = results)  #    this form is also embedded in this container

@app.route("/save", methods=["GET", "POST"])
def save():
    if request.method == "POST":
        nickname = request.form['nickname']
        id = request.form['number']
        pokemon = poke.create_pokemon(strip_zeros(id))
        db.addPokemon(pokemon.name, nickname, pokemon.number, pokemon.height, pokemon.weight, \
            pokemon.type1, pokemon.type2, pokemon.ability1, pokemon.ability2, pokemon.image_png)
        msg = "Pokémon " + pokemon.name + " (" + pokemon.number + ") caught!"
        img = pokemon.image_png
        return render_template("success.html", msg = msg, img=img)

def generate_random_pokemon():
    exists = True
    while exists:
        number = randint(0,898)
        str_number = str(poke.append_zeros(number))
        conn = db.sqlite3.connect('pokeDB.db')
        c = conn.cursor()
        c.execute("SELECT * FROM pokemon WHERE number = " + str_number)
        results = c.fetchall()             
        c.close()                         
        conn.close()    
        # check if it is empty so you know you haven't caught it yet
        if not results:
            exists = False
            pokemon = poke.create_pokemon(number)
            return pokemon

def strip_zeros(number):
    return number.lstrip('0')

if __name__ == "__main__":
    # print("Directory {} contains: \n".format(os.getcwd()))
    # print(os.listdir(os.getcwd()))
    if os.path.exists('pokeDB.db'):
        print ("Deleting old versions of pokeDB.db from the {} directory".format(os.getcwd()))
        os.remove('pokeDB.db')    # delete any old versions - don't use if you need persistence!

    db.createDB()
    app.run(host='0.0.0.0')    # start up the flask server
