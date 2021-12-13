import os
import sqlite3
from random import randint

### exampleDB3.py
#
## Simple (fat-finger) flask application.  The application acts as the SQL "backend"
#
#  This program is called from main.py and provides the functionality needed 
# to create (the DB and a basic table), start, and perform CRUD operations on the
# database contents 
#


def createDB():
#  
# createDB() creates a DB table and prepopulates it with a list of Dicts
#
#
    nameList = [{'Name':'Squirtle', 'Nickname':'Bubbles', 'Number':'007', 'Height':5, 'Weight':90, 'Type1':'Water', 'Type2':'-', 'Ability1':'Torrent', 'Ability2':'Rain-dish' , 'Image':'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png'},
                {'Name':'Ivysaur', 'Nickname':'Bubbles', 'Number':'010', 'Height':10, 'Weight':130, 'Type1':'Grass', 'Type2':'Poison', 'Ability1':'Overgrow', 'Ability2':'Chlorophyll' , 'Image':'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/2.png'}

                ]

    conn = sqlite3.connect('pokeDB.db')      # connect to the pokemon database
    c = conn.cursor()                          # create the cursor - we work from the cursor object
    c.execute("CREATE TABLE IF NOT EXISTS pokemon(Id INTEGER PRIMARY KEY, Name TEXT, Nickname TEXT, Number TEXT, Height INTEGER, Weight INTEGER, Type1 TEXT, Type2 TEXT,\
              Ability1 TEXT, Ability2 TEXT, Image TEXT)")
    conn.commit()                               # execute the table creation

    for item in nameList:
        print("Inserting: ", item['Name'], item['Nickname'], item['Number'], item['Height'], item['Weight'], item['Type1'], item['Type2'], item['Ability1'], item['Ability2'], item['Image'])
        c.execute("INSERT INTO pokemon(Name, Nickname, Number, Height, Weight, Type1, Type2,\
              Ability1, Ability2, Image) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", \
                  (item['Name'], item['Nickname'], item['Number'], item['Height'], \
                   item['Weight'], item['Type1'], item['Type2'], item['Ability1'], \
                   item['Ability2'], item['Image']))
        conn.commit()
 
    print("\nList of Pokemon complete, {0} names were inserted",len(nameList))
    c.close()            # Close the cursor
    conn.close()         # Shut down the connection to the DB


def addPokemon(Name, Nickname, Number, Height, Weight, Type1, Type2, Ability1, Ability2, Image):
    #
    # (id INTEGER PRIMARY KEY, fName , lName, position, number, drafted)
    # Called by main save() function.  It just inserts the arguments that were passed in
    # as new entries into the DB
    # 
    conn = sqlite3.connect('pokeDB.db')     # connect to the database
    c = conn.cursor()                         # create the cursor
    c.execute("INSERT INTO pokemon(Name, Nickname, Number, Height, Weight, Type1, Type2,\
              Ability1, Ability2, Image) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", \
                  (Name, Nickname, Number, Height, Weight, Type1, Type2, Ability1, Ability2, Image))
    conn.commit()

    c.close()            # Close the cursor
    conn.close()         # Shut down the connection to the DB

#
# Dump all players in table
#
def getPokemon():
    #
    # (id INTEGER PRIMARY KEY, fName , lName, position, number, drafted)
    # Called by the main list() function call
    #  it just retrieves all of the entries in the table and returns them to
    #  list() - list() will then send them back to the browser
    #
    conn = sqlite3.connect('pokeDB.db')     # connect to the database
    c = conn.cursor()                         # create the cursor
    c.execute("SELECT * FROM pokemon")   # pull everything in the eagles table
    results = c.fetchall()
    c.close()            # Close the cursor
    conn.close()         # Shut down the connection to the DB

    return results       # return a list from the fetchall() call

# Example DELETE clause
#     
def deletePokemon(number):
    #
    # (id INTEGER PRIMARY KEY, fName , lName, position, number, drafted)
    #
    conn = sqlite3.connect('pokeDB.db')     # connect to the database
    c = conn.cursor()                         # create the cursor
    c.execute("DELETE FROM pokemon WHERE number=?",(number,))  #remember the , for the TUPLE!
    conn.commit()
    c.execute("SELECT * FROM pokemon")
    results= c.fetchall()
    c.close()            # Close the cursor
    conn.close()         # Shut down the connection to the DB
    return results

##
# We are importing this into another program but if you wanted to
#  make this a standalone program to handle database functions
#  Just uncomment the python program entry point below
#  
# if __name__ == "__main__":          
#     createDB()
