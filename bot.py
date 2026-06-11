import discord
from discord.ext import commands

TOKEN = ""

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

# ---- CONFIG: STAFF ROLES ----
STAFF_ROLES = ["Staff"]

# ---- PERMISSION CHECK ----
def staff_only():
    async def predicate(ctx):

        # Server owner always allowed
        if ctx.author == ctx.guild.owner:
            return True

        # Administrator always allowed
        if ctx.author.guild_permissions.administrator:
            return True

        # Staff roles allowed
        return any(role.name in STAFF_ROLES for role in ctx.author.roles)

    return commands.check(predicate)

# ---- BOT READY ----
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# ---- COMMANDS ----

@bot.command()
@staff_only()
async def cash(ctx):
    await ctx.send("💵 Cash App: urtag")

@bot.command()
@staff_only()
async def paypal(ctx):
    await ctx.send("💳 PayPal: urtag")

@bot.command()
@staff_only()
async def venmo(ctx):
    await ctx.send("📱 Venmo: urtag")

@bot.command()
@staff_only()
async def methods(ctx):
    await ctx.send(
        "💰 Payment Methods\n"
        "💵 Cash App: urtag\n"
        "💳 PayPal: urtag\n"
        "📱 Venmo: urtag"
    )

# ---- ERROR HANDLER (optional but helpful) ----
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("❌ You don’t have permission to use this command.")

# ---- RUN BOT ----
bot.run(TOKEN)
