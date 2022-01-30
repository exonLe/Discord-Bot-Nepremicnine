import sqlite3


class DB_SQL:
    """Class for insearting and reading in and from SQLite database"""

    def __init__(self, neprId=1):
        self.neprId = neprId
        self.connection = sqlite3.connect("SQLite_Python.db")

        cursor = self.connection.cursor()
        try:
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS nepremicnine(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                link TEXT NOT NULL);"""
            )

        except sqlite3.Error as error:  # In case of an error
            print("Error while creating a sqlite table", error)

    def __del__(self):
        self.connection.close()

    def updateSqliteTable(self, link):
        """Update data in DB"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """UPDATE nepremicnine1 SET link = ? where id = ?""",
                (link, self.neprId),
            )
            self.connection.commit()

        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)

    def read_link(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """SELECT * from nepremicnine1 where id = ?""", (self.neprId,)
            )
            record = cursor.fetchone()
            return record[1]
        except sqlite3.Error as error:
            print("Failed to read single row from sqlite table", error)
            return ""
