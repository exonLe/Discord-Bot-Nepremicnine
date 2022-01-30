import sqlite3
from data_pull import Neprweb1


def updateSqliteTable(id, link):
    """UPDATE DATA IN TABLE"""
    try:
        sqliteConnection = sqlite3.connect("SQLite_Python.db")
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """UPDATE nepremicnine1 SET link = ? where id = ?"""
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
nepr_link = Neprweb1()  # Link to the latest apartment
