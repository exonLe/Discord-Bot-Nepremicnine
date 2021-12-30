import sqlite3
from data_pull import Neprweb1, nepremicne_web


################## INSERT DATA INTO TABLE - uncomment for fresh table ########################################

nepr_link = Neprweb1() #Link to the latest apartment
'''
def insertVaribleIntoTable(id, link):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db') #Connect to DB
        cursor = sqliteConnection.cursor() ##create a cursor object to execute SQLite command/queries from Python
        print("Successfully Connected to SQLite")

        #Insert into table - parameters
        sqlite_insert_with_param = """INSERT INTO nepremicnine
                            (id, link) 
                            VALUES (?, ?);"""


        data_tuple = (id, link)
        cursor.execute(sqlite_insert_with_param, data_tuple) #Run the SQL query and return the result
        sqliteConnection.commit() #Commit changes
        print("Record inserted successfully into nepremicnine table ", cursor.rowcount)

        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")

##DATA
insertVaribleIntoTable(None, nepr_link) #Inserts Link with new ID into table
'''

################## UPDATE DATA IN TABLE ########################################

def updateSqliteTable(id, link):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """UPDATE nepremicnine SET link = ? where id = ?"""
        data = (link, id)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        print("Record Updated successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The sqlite connection is closed")

# Function that is called in nepremicnine_bot_discord.py to update table: 
# updateSqliteTable(1, nepr_link) #Update link with ID = 1
