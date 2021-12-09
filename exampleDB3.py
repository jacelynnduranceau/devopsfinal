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
    nameList = [{'fName':'Nick', 'lName':'Foles', 'position':'QB', 'number':9, 'drafted':'yes'},
                    {'fName':'Carson', 'lName':'Wentz', 'position':'QB', 'number':11, 'drafted':'yes'},
                    {'fName':'Jalen', 'lName':'Hurts', 'position':'QB', 'number':2, 'drafted':'yes'},
                    {'fName':'Jalen', 'lName':'Reagor', 'position':'WR', 'number':18, 'drafted':'yes'},
                    {'fName':'Travis', 'lName':'Fulgham', 'position':'WR', 'number':13, 'drafted':'yes'},
                    {'fName':'Fletcher', 'lName':'Cox', 'position':'DE', 'number':91, 'drafted':'yes'},
                    {'fName':'Zach', 'lName':'Ertz', 'position':'TE', 'number':86, 'drafted':'yes'},
                    {'fName':'Joe', 'lName':'Flacco', 'position':'QB', 'number':0, 'drafted':'yes'},
                    {'fName':'Darius', 'lName':'Slay', 'position':'CB', 'number':24, 'drafted':'yes'},
                    {'fName':'Jordan', 'lName':'Mailata', 'position':'RT', 'number':68, 'drafted':'yes'},
                    {'fName':'Alex', 'lName':'Singleton', 'position':'LB', 'number':49, 'drafted':'yes'},
                    {'fName':'Dallas', 'lName':'Goedert', 'position':'TE', 'number':88, 'drafted':'yes'},
                        ]

    conn = sqlite3.connect('eaglesDB.db')      # connect to the eagles database
    c = conn.cursor()                          # create the cursor - we work from the cursor object
    
    c.execute("CREATE TABLE IF NOT EXISTS eagles(id INTEGER PRIMARY KEY, fName TEXT, lName TEXT, position TEXT, number INTEGER, drafted TEXT)")
    conn.commit()                               # execute the table creation

    id = 0
    for item in nameList:
        id += 1
        print("Inserting: ", id, item['fName'], item['lName'], item['position'], item['number'], item['drafted'])
        c.execute("INSERT INTO eagles VALUES(?, ?, ?, ?, ?, ?)", (id, item['fName'], item['lName'], item['position'], item['number'], item['drafted']))
        conn.commit()
 
    print("\nList of Eagles players complete, {0} names were inserted",len(nameList))
    c.close()            # Close the cursor
    conn.close()         # Shut down the connection to the DB


def addPlayer(fname, lname, pos, num, draft):
    #
    # (id INTEGER PRIMARY KEY, fName , lName, position, number, drafted)
    # Called by main save() function.  It just inserts the arguments that were passed in
    # as new entries into the DB
    # 
    id = randint(25,63)
    conn = sqlite3.connect('eaglesDB.db')     # connect to the database
    c = conn.cursor()                         # create the cursor
    c.execute("INSERT INTO eagles VALUES(?, ?, ?, ?, ?, ?)",(id, fname, lname, pos, num, draft))
    conn.commit()

    c.close()            # Close the cursor
    conn.close()         # Shut down the connection to the DB

#
# Dump all players in table
#
def getPlayers():
    #
    # (id INTEGER PRIMARY KEY, fName , lName, position, number, drafted)
    # Called by the main list() function call
    #  it just retrieves all of the entries in the table and returns them to
    #  list() - list() will then send them back to the browser
    #
    conn = sqlite3.connect('eaglesDB.db')     # connect to the database
    c = conn.cursor()                         # create the cursor
    c.execute("SELECT * FROM eagles")   # pull everything in the eagles table
    results = c.fetchall()
    c.close()            # Close the cursor
    conn.close()         # Shut down the connection to the DB

    return results       # return a list from the fetchall() call

# Example DELETE clause
#     
def deletePlayer(number):
    #
    # (id INTEGER PRIMARY KEY, fName , lName, position, number, drafted)
    #
    conn = sqlite3.connect('eaglesDB.db')     # connect to the database
    c = conn.cursor()                         # create the cursor
    c.execute("DELETE FROM eagles WHERE number=?",(number,))  #remember the , for the TUPLE!

    c.execute("SELECT * FROM eagles")
    results= c.fetchall()

    c.close()            # Close the cursor
    conn.close()         # Shut down the connection to the DB

##
# We are importing this into another program but if you wanted to
#  make this a standalone program to handle database functions
#  Just uncomment the python program entry point below
#  
# if __name__ == "__main__":          
#     createDB()