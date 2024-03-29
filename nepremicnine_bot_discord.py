import discord
import asyncio

from data_pull import Neprweb1
from read_DB import read_link
from insert_and_update_DB import updateSqliteTable


TOKEN = ''


class MyClient(discord.Client):
    ''' ######  MAKE BOT ONLINE ####### '''

    async def on_ready(self):
        print(f'{client.user} is now online!')

    async def on_message(self, message):
        # Don't respond to ourselves - we don't want to loop bot
        if message.author == self.user:
            return
        # Lower case message
        message_content = message.content.lower()

        # Send bot info for options
        if message.content == 'info':
            await message.channel.send('options: $realtime, nepremicnine, stanovanje')

        # Send bot nepremicnine for general real-estate link
        if message.content == 'nepremicnine':
            await message.channel.send('https://www.nepremicnine.net/oglasi-oddaja/ljubljana-mesto/stanovanje/')

        # Get from data_pull, the last apartment that was published
        if message.content == 'stanovanje':
            zadnje_stanovanje = Neprweb1()
            if zadnje_stanovanje != read_link(): #Check if link is the same
                updateSqliteTable(1, zadnje_stanovanje) #Update table
            await message.channel.send(zadnje_stanovanje) #Send a message back to the user in the same channel
        ######################

        if '$realtime' in message_content: #Write $realtime to chat bot, to get realtime feedback
            while True:
                zadnje_stanovanje = Neprweb1()
                if zadnje_stanovanje != read_link(): #Check if link is the same
                    updateSqliteTable(1, zadnje_stanovanje) #Update table
                    await message.channel.send('nova nepremicnina link')
                    await message.channel.send(zadnje_stanovanje) #Send a message back to the user in the same channel
                    print("nova nepremicnina link \n")
                await asyncio.sleep(600)


if __name__ == '__main__':
    client = MyClient()
    client.run(TOKEN)

##vsako uro (1h) naredi request in pogleda, če je link, ki ga dobi isti(pogleda v bazo-sqllite), (if) če je isti ne naredi nič, če je nov, ga pošlje.

