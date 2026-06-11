import discord
from discord.ext import commands

TOKEN = ""

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.command()
async def cash(ctx):
    await ctx.send(
        "**💵 Cash App Payment Information**\n"
        "Cash App: $313Beg"
    )

@bot.command()
async def paypal(ctx):
    await ctx.send(
        "**💳 PayPal Payment Information**\n"
        "PayPal: malikwarefr@gmail.com"
    )

@bot.command()
async def venmo(ctx):
    await ctx.send(
        "**📱 Venmo Payment Information**\n"
        "Venmo: @MalikWarefr"
    )

@bot.command()
async def payment(ctx):
    await ctx.send(
        "**💰 Payment Methods**\n"
        "💵 Cash App: $313Beg\n"
        "💳 PayPal: malikwarefr@gmail.com\n"
        "📱 Venmo: @MalikWareFr"
    )

bot.run(TOKEN)

@bot.event
async def on_ready():
    print("Bot is online")