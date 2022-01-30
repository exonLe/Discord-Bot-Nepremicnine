import sqlite3


def main():
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


if __name__ == "__main__":
    main()
