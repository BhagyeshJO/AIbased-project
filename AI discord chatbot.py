
import discord
import os
from openai import OpenAI
import openai
from secret import OPENAI_API_KEY

print(OPENAI_API_KEY)
openai.api_key = os.getenv(OPENAI_API_KEY)

token= os.getenv(TOKEN)

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if self.user != message.author:
            if self.user in message.mentions:
                channel = message.channel
                response = openai.completions.create(

                  model="gpt-3.5-turbo",
                  prompt= message.content,
                  temperature=1,
                  max_tokens=256,
                  top_p=1,
                  frequency_penalty=0,
                  presence_penalty=0
                )
                messageToSend = response.choices[0].text
                await channel.send(response.choices[0].text)


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token)
