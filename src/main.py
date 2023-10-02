import discord
import responses

async def send_message(message, user_message):
    if not user_message.strip():
        print("Received an empty message.")
    else:
        try:
            response = responses.handle_response(user_message)
            if response:
                await message.channel.send(response)
            else:
                print(f"Empty response for message: {user_message}")
        except discord.Forbidden:
            print("Permission error: bot can't send messages.")
        except Exception as e:
            print(e)

def run_bot():
    TOKEN = 'MTE1NzQ2NDM1MDg0ODcyNTAwMg.GrXEqi.4aLMJtmDN_RlfPokj_n9FKx0Wp5jIUUSQS3sGg'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)

        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        await send_message(message, user_message)

    client.run(TOKEN)

if __name__ == '__main__':
    run_bot()
