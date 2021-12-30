import sqlite3


neprId = 1 #Define row ID

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")

    sqlite_select_query = """SELECT * from nepremicnine where id = ?"""
    cursor.execute(sqlite_select_query, (neprId,))
    print("Reading single row \n")
    record = cursor.fetchone()
    print("Id: ", record[0])
    print(record[1])
    
    cursor.close()

except sqlite3.Error as error:
    print("Failed to read single row from sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")


readed_link = record[1] #Link[1] that we get from our Table nepremicnine
