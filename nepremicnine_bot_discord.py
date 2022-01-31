""" vsako uro (1h) naredi request in pogleda, če je link, ki ga dobi isti(pogleda v bazo-sqllite), \
    (if) če je isti ne naredi nič, če je nov, ga pošlje.
"""

try:
    from discord import Client
except ModuleNotFoundError:

    class Client:
        """Dummy class if discord is not installed"""

        def run(*_):
            """Empty fn"""
            print("ERROR: Unable to import discord Client")
            return _


import asyncio
import os
import sys
import sqlite3

from data_pull import Neprweb1


class DB_SQL:
    """Class for insearting and reading in and from SQLite database"""

    def __init__(self, nid=1):
        self.nid = nid
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

    def update_table(self, link):
        """Update data in DB"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                """UPDATE nepremicnine1 SET link = ? where id = ?""",
                (link, self.nid),
            )
            self.connection.commit()

        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)

    def read_link(self):
        """Returns last link in database if existing"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""SELECT * from nepremicnine1 where id = ?""", (self.nid,))
            record = cursor.fetchone()
            return record[1]
        except sqlite3.Error as error:
            print("Failed to read single row from sqlite table", error)
            return ""


class MyClient(Client):
    """MAKE BOT ONLINE"""

    async def on_ready(self):
        print(f"{self.user} is now online!")

    async def on_message(self, message):
        # Don't respond to ourselves - we don't want to loop bot
        if message.author == self.user:
            return
        # Lower case message
        message_content = message.content.lower()

        # Send bot info for options
        if message.content == "info":
            await message.channel.send("options: $realtime, nepremicnine, stanovanje")

        # Send bot nepremicnine for general real-estate link
        if message.content == "nepremicnine":
            await message.channel.send(
                "https://www.nepremicnine.net/oglasi-oddaja/ljubljana-mesto/stanovanje/"
            )

        # Get from data_pull, the last apartment that was published
        if message.content == "stanovanje":
            zadnje_stanovanje = Neprweb1()
            if zadnje_stanovanje != db.read_link():  # Check if link is the same
                db.update_table(zadnje_stanovanje)  # Update table
            await message.channel.send(
                zadnje_stanovanje
            )  # Send a message back to the user in the same channel
        ######################

        if (
            "$realtime" in message_content
        ):  # Write $realtime to chat bot, to get realtime feedback
            while True:
                zadnje_stanovanje = Neprweb1()
                if zadnje_stanovanje != db.read_link():  # Check if link is the same
                    db.update_table(zadnje_stanovanje)  # Update table
                    await message.channel.send("nova nepremicnina link")
                    await message.channel.send(
                        zadnje_stanovanje
                    )  # Send a message back to the user in the same channel
                    print("nova nepremicnina link \n")
                await asyncio.sleep(600)


if __name__ == "__main__":
    if "TOKEN" not in os.environ:
        print("ERROR: insert token or pass by env variable")
        sys.exit(1)

    db = DB_SQL()
    client = MyClient()
    client.run(os.environ["TOKEN"])
