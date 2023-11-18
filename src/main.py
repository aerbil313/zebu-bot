import sys
import discord
from random import choice
from zebu_patterns import patterns

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <BOT_TOKEN>")
        sys.exit(1)

    token = sys.argv[1]

    bot = discord.Bot()

    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user.name}")
        print(f"Running with token: {token}")

    @bot.slash_command(description="Generate a zebu prompt.")
    async def zebu(ctx):
        key = choice(list(patterns.keys()))
        response = key + "\n" + patterns[key]
        await ctx.respond(response)

    @bot.slash_command(description="List all zebu prompts.")
    async def zebu_list_patterns(ctx):
        r = 1
        response = ""
        for i, x in patterns.items():
            response += f"{r}. {i}\n"
            r += 1
        await ctx.respond(response)

    bot.run(token)
