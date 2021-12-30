import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db') #Connect to DB
    #Create table
    sqlite_create_table_query = '''CREATE TABLE nepremicnine (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                link TEXT NOT NULL);'''

    cursor = sqliteConnection.cursor() ##Create a cursor object to execute SQLite command/queries from Python
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query) #Run the SQL query and return the result
    sqliteConnection.commit() #Commit changes
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error: #In case of an error
    print("Error while creating a sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close() #Close connection
        print("sqlite connection is closed")