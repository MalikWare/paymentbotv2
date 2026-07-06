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

# ---- EMBED FUNCTION ----
def create_payment_embed(title, value, icon="💳"):
    embed = discord.Embed(
        title=f"{icon} {title}",
        description=value,
        color=discord.Color.blue()
    )

    embed.set_footer(
        text="Payment Information",
        icon_url=bot.user.display_avatar.url if bot.user else None
    )

    return embed

# ---- COMMANDS ----

@bot.command()
@staff_only()
async def cash(ctx):
    embed = create_payment_embed(
        "Cash App",
        "```URTAG```",
        "💵"
    )
    await ctx.send(embed=embed)

@bot.command()
@staff_only()
async def paypal(ctx):
    embed = create_payment_embed(
        "PayPal",
        "```URTAG```",
        "💰"
    )
    await ctx.send(embed=embed)

@bot.command()
@staff_only()
async def venmo(ctx):
    embed = create_payment_embed(
        "Venmo",
        "```URTAG ```",
        "🏦"
    )
    await ctx.send(embed=embed)

@bot.command()
@staff_only()
async def methods(ctx):
    embed = discord.Embed(
        title="💳 Payment Methods",
        description="Available payment options",
        color=discord.Color.green()
    )

    embed.add_field(
        name="💵 Cash App",
        value="```URTAG```",
        inline=False
    )

    embed.add_field(
        name="💰 PayPal",
        value="```URTAG```",
        inline=False
    )

    embed.add_field(
        name="🏦 Venmo",
        value="```URTAG ```",
        inline=False
    )

    embed.set_thumbnail(url=ctx.guild.icon.url if ctx.guild.icon else discord.Embed.Empty)

    embed.set_footer(
        text=f"Requested by {ctx.author}",
        icon_url=ctx.author.display_avatar.url
    )

    await ctx.send(embed=embed)

# ---- ERROR HANDLER ----
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            title="❌ Access Denied",
            description="You do not have permission to use this command.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

# ---- RUN BOT ----
bot.run(TOKEN)
