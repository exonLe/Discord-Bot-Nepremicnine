import sqlite3


def check_DB():
    try:
        sqliteConnection = sqlite3.connect(
            "SQLite_Python.db"
        )  # Connect and create DB if it is not existing
        cursor = (
            sqliteConnection.cursor()
        )  # Create a cursor object to execute SQLite command/queries from Python
        print("Database created and Successfully Connected to SQLite")

        sqlite_select_Query = "select sqlite_version();"
        cursor.execute(sqlite_select_Query)  # Run the SQL query and return the result
        record = cursor.fetchall()  # Read query results
        print("SQLite Database Version is: ", record)
        cursor.close()

    except sqlite3.Error as error:  # In case of an error
        print("Error while connecting to sqlite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()  # Close connection
            print("The SQLite connection is closed")


def init_DB():
    try:
        sqliteConnection = sqlite3.connect("SQLite_Python.db")  # Connect to DB
        # Create table
        sqlite_create_table_query = """CREATE TABLE nepremicnine (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    link TEXT NOT NULL);"""

        cursor = (
            sqliteConnection.cursor()
        )  # Create a cursor object to execute SQLite command/queries from Python
        print("Successfully Connected to SQLite")
        cursor.execute(
            sqlite_create_table_query
        )  # Run the SQL query and return the result
        sqliteConnection.commit()  # Commit changes
        print("SQLite table created")

        cursor.close()

    except sqlite3.Error as error:  # In case of an error
        print("Error while creating a sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()  # Close connection
            print("sqlite connection is closed")


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


def read_link():
    neprId = 1  # Define row ID
    try:
        sqliteConnection = sqlite3.connect("SQLite_Python.db")
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")

        sqlite_select_query = """SELECT * from nepremicnine1 where id = ?"""
        cursor.execute(sqlite_select_query, (neprId,))
        # print("Reading single row \n")
        record = cursor.fetchone()
        # print("Id: ", record[0])
        # print(record[1])
        cursor.close()
        return record[1]  # Link[1] that we get from our Table nepremicnine

    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")
