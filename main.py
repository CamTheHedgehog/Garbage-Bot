import os
import discord
from discord.ui import Button, View
import random
import time
from discord import app_commands
import sys
import consts
from role_management import RoleInfo, send_roles_callback


intents = discord.Intents.default()
intents.members = True


# Definitions
frank_jpegs = []


async def sendButtonPingRoles():
    roles = [
        RoleInfo(
            "General Announcements",
            "🔔",
            1043020516346302504,
        ),
        RoleInfo(
            "DankPods",
            "<:dankpods:1040417450686173184>",
            1043016550103384064,
        ),
        RoleInfo(
            "Garbage Time",
            "<:tony:1040419706399625266>",
            1043016644412317776,
        ),
        RoleInfo(
            "Garbage Stream (Morn)",
            "<:chonkfronk:1040418775129927752>",
            1043016713677053982,
        ),
        RoleInfo(
            "Garbage Stream (Arvo)",
            "<:shrek:1040482904414879826>",
            1043020552878702612,
        ),
        RoleInfo(
            "The Drum Thing",
            "<:drumthing:1041177501604515960>",
            1043016786100101240,
        ),
        RoleInfo(
            "Polls",
            "📊",
            1044037090066833508,
        ),
    ]

    await send_roles_callback(client, roles, "Ping Roles")


async def sendButtonTonaRoles():
    """
    Allow users to add or remove the various Tona roles
    """
    the_tonas = [
        RoleInfo(
            "OG Tona",
            "<:tonatime:1040858187592642622>",
            1043018409560002580,
            give_message="DAYTONNNAAAAAAAAAAAA",
        ),
        RoleInfo(
            "Sky Hihi",
            "☁️",
            1043018486823272448,
            give_message="I haven't heard this one yet, so idk what to put here",
        ),
        RoleInfo(
            "Rollo Finito",
            "🏁",
            1043018524324540478,
            give_message="ROLLLLLING FRAAAANNNNNKKKKKK",
        ),
    ]

    await send_roles_callback(client, the_tonas, "Tona Roles")


# async def sendDropdownTZRoles():
#     select = Select(options=[
#         discord.SelectOption(label="GMT-12:00", emoji="🕛"),
#         discord.SelectOption(label="GMT-11:00", emoji="🕚"),
#         discord.SelectOption(label="GMT-10:00", emoji="🕙"),
#         discord.SelectOption(label="GMT-9:00", emoji="🕘"),
#         discord.SelectOption(label="GMT-8:00", emoji="🕗"),
#         discord.SelectOption(label="GMT-7:00", emoji="🕖"),
#         discord.SelectOption(label="GMT-6:00", emoji="🕕"),
#         discord.SelectOption(label="GMT-5:00", emoji="🕔"),
#         discord.SelectOption(label="GMT-4:00", emoji="🕓"),
#         discord.SelectOption(label="GMT-3:00", emoji="🕒"),
#         discord.SelectOption(label="GMT-2:00", emoji="🕑"),
#         discord.SelectOption(label="GMT-1:00", emoji="🕐"),
#         discord.SelectOption(label="GMT±0:00", emoji="<a:animated_clock:562493945058164739>"),
#         discord.SelectOption(label="GMT+1:00", emoji="🕐"),
#         discord.SelectOption(label="GMT+2:00", emoji="🕑"),
#         discord.SelectOption(label="GMT+3:00", emoji="🕒"),
#         discord.SelectOption(label="GMT+3:30", emoji="🕞"),
#         discord.SelectOption(label="GMT+4:00", emoji="🕓"),
#         discord.SelectOption(label="GMT+4:30", emoji="🕟"),
#         discord.SelectOption(label="GMT+5:00", emoji="🕔"),
#         discord.SelectOption(label="GMT+5:30", emoji="🕠"),
#         discord.SelectOption(label="GMT+6:00", emoji="🕕"),
#         discord.SelectOption(label="GMT+6:30", emoji="🕡"),
#         discord.SelectOption(label="GMT+7:00", emoji="🕖"),
#         discord.SelectOption(label="GMT+8:00", emoji="🕗")
#     ])
#     select2=Select(options=[
#         discord.SelectOption(label="GMT+9:00", emoji="🕘"),
#         discord.SelectOption(label="GMT+9:30", emoji="🕤"),
#         discord.SelectOption(label="GMT+10:00", emoji="🕙"),
#         discord.SelectOption(label="GMT+10:30", emoji="🕥"),
#         discord.SelectOption(label="GMT+11:00", emoji="🕚"),
#         discord.SelectOption(label="GMT+12:00", emoji="🕛"),
#         discord.SelectOption(label="GMT+13:00", emoji="3️⃣"),
#         discord.SelectOption(label="GMT+14:00", emoji="4️⃣")
#     ])
#
#     async def timezoneCallback(interaction):
#         if select.values == True:
#             if select.values[0] == "GMT-12:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045189927954026537)
#             elif select.values[0] == "GMT-11:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045189924883808278)
#             elif select.values[0] == "GMT-10:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045189921905848320)
#             elif select.values[0] == "GMT-9:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045189918806261810)
#             elif select.values[0] == "GMT-8:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045189915257872444)
#             elif select.values[0] == "GMT-7:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045189909733974026)
#             elif select.values[0] == "GMT-6:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045189905971679283)
#             elif select.values[0] == "GMT-5:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045189901970313219)
#             elif select.values[0] == "GMT-4:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045189897004257291)
#             elif select.values[0] == "GMT-3:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045189725679534101)
#             elif select.values[0] == "GMT-2:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045189620712865882)
#             elif select.values[0] == "GMT-1:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045188897325461554)
#             elif select.values[0] == "GMT±0:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045186821384065045)
#             elif select.values[0] == "GMT+1:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045190313519616050)
#             elif select.values[0] == "GMT+2:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045190317550354442)
#             elif select.values[0] == "GMT+3:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045190325699891240)
#             elif select.values[0] == "GMT+3:30":
#                 role = client.get_guild(consts.GUILD).get_role(1045196700156952628)
#             elif select.values[0] == "GMT+4:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045190328703000596)
#             elif select.values[0] == "GMT+4:30":
#                 role = client.get_guild(consts.GUILD).get_role(1045196824501309481)
#             elif select.values[0] == "GMT+5:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045190332041678959)
#             elif select.values[0] == "GMT+5:30":
#                 role = client.get_guild(consts.GUILD).get_role(1045196973822726246)
#             elif select.values[0] == "GMT+6:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045190335971721237)
#             elif select.values[0] == "GMT+6:30":
#                 role = client.get_guild(consts.GUILD).get_role(1045197080844578866)
#             elif select.values[0] == "GMT+7:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045190339163594812)
#             elif select.values[0] == "GMT+8:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045190342351257691)
#             elif select2.values[0] == "GMT+9:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045190345157246997)
#             elif select2.values[0] == "GMT+9:30":
#                 role = client.get_guild(consts.GUILD).get_role(1045197227041226762)
#             elif select2.values[0] == "GMT+10:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045190348437196851)
#             elif select2.values[0] == "GMT+10:30":
#                 role = client.get_guild(consts.GUILD).get_role(1045197320888787005)
#             elif select2.values[0] == "GMT+11:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045190353474555914)
#             elif select2.values[0] == "GMT+12:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045190356741935145)
#             elif select2.values[0] == "GMT+13:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045190359870869634)
#             elif select2.values[0] == "GMT+14:00":
#                 role = client.get_guild(consts.GUILD).get_role(1045190363889016864)

#             member = client.get_guild(consts.GUILD).get_member(interaction.user.id)
#             if role == True:
#                 if role.members.__contains__(member):
#                     await member.remove_roles(role)
#                     await interaction.response.send_message("Removed \""+role.name()+"\" Role", ephemeral=True)
#                 else:
#                     await member.add_roles(role)
#                     await interaction.response.send_message("You have been given the \""+role.name()+"\" Role", ephemeral=True)

#     select.callback = timezoneCallback
#     select2.callback = timezoneCallback
#     view=View()
#     view.add_item(select)
#     view.add_item(select2)
#     await client.get_channel(1043016204278829066).send(content='Select the Option for your respective *Time Zone*',embed=discord.Embed(title='Time Zone Help', description='Calculate the amount of hours since Jan 1st 1970\n\n<t:0>', color=discord.Color.green()),view=view)


# Activate Bot

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=intents,)

    async def on_ready(self):
        await self.wait_until_ready()
        self.synced = False
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=consts.GUILD))
            self.synced = True
            print('Commands Synced')
        print(f'Bot is online')
        if 'debug' in os.listdir('./'):
            await client.change_presence(activity=discord.Game(name="DEBUG MODE"))
            print('Bot Presence changed to \"Playing DEBUG MODE\"')
            await client.get_channel(1061732002275016745).send(embed=discord.Embed(
                title='Online Status',
                description=f'Bitey Frank Online Since <t:{str(int(time.time()))}:R> <@&1065773538281259009>',
                color=discord.Color.green()
            ))
        else:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="my stinky poos"))
            print('Bot Presence changed to \"Watching my stinky poos\"')
            await client.get_channel(1061732002275016745).send(embed=discord.Embed(
                title='Online Status',
                description=f'Bitey Frank Online Since <t:{str(int(time.time()))}:R>',
                color=discord.Color.green()
            ))

        ### CONTRIBUTERS, If you see this would you be able to make this loop every 10 minutes? ###
        await client.get_channel(1043016204278829066).purge()
        await sendButtonPingRoles()
        await sendButtonTonaRoles()
        # await sendDropdownTZRoles()
        ###########################################################################################


client = aclient()

for frankJpeg in os.listdir('beajpeg-assets'):
    if frankJpeg.endswith(('jpg', 'jpeg', 'png', 'webp', 'gif')):
        frank_jpegs.append(f'beajpeg-assets/{frankJpeg}')
    else:
        client.get_channel(
            '1061732002275016745'
        ).send(
            f'Warning, file \"{frankJpeg}\" is not a supported Frank JPEG'
        )


@client.event
async def on_member_join(member):
    """Welcome users"""
    await client.get_channel(1030635476245286978).send(random.choice(frankJoinEmotes))
    print(f'Greeted {member}')


@client.event
async def on_member_remove(member):
    """Say goodbye to users"""
    await client.get_channel(1030635476245286978).send(f"{member.mention} <:frank:1040418489476853872>7")
    print(f'Said goodbye to {member}')


# Commands

tree = app_commands.CommandTree(client)


@tree.command(
    name="beajpeg",
    description="Make frank be a .jpeg",
    guild=discord.Object(id=consts.GUILD)
)
async def self(Interaction: discord.Interaction):
    await Interaction.response.send_message(file=discord.File(random.choice(frank_jpegs)))
    print('Ran /beajpeg')


@tree.command(
    name='frankjpeg',
    description=f'Choose a specific frank .jpeg (out of 0 to {str(len(frank_jpegs)-1)})',
    guild=discord.Object(id=consts.GUILD)
)
async def self(Interaction: discord.Interaction, option: int):
    await Interaction.response.send_message(file=discord.File(frank_jpegs[option]))
    print('Ran /frankjpeg')


@tree.command(
    name='listfrankjpegs',
    description='List the Frank .jpegs',
    guild=discord.Object(id=consts.GUILD)
)
async def self(Interaction: discord.Interaction):
    message = 'Frank jpegs:'
    id = 0
    for jpegName in frank_jpegs:
        message += f'\n*{str(id)}*: **__{jpegName[15:]}__**'
        id += 1
    await Interaction.response.send_message(message)
    print('Ran /listfrankjpegs')


# Polling

@tree.command(
    name='poll',
    description='Make a poll',
    guild=discord.Object(id=consts.GUILD))
async def embed(Interaction: discord.Interaction, question: str, option1: str, option2: str, option3: str = None, option4: str = None, option5: str = None, option6: str = None, option7: str = None, option8: str = None, option9: str = None, option10: str = None):
    await Interaction.response.send_message('Creating Poll', ephemeral=True)
    description = '1️⃣ '+option1+'\n\n2️⃣ '+option2

    if option3 != None:
        description += '\n\n3️⃣ '+option3
    if option4 != None:
        description += '\n\n4️⃣ '+option4
    if option5 != None:
        description += '\n\n5️⃣ '+option5
    if option6 != None:
        description += '\n\n6️⃣ '+option6
    if option7 != None:
        description += '\n\n7️⃣ '+option7
    if option8 != None:
        description += '\n\n8️⃣ '+option8
    if option9 != None:
        description += '\n\n9️⃣ '+option9
    if option10 != None:
        description += '\n\n🔟 '+option10

    poll = await client.get_channel(Interaction.channel_id).send(
        embed=discord.Embed(
            title=question,
            description=description,
            color=discord.Color.green()
        ).set_author(
            name=Interaction.user.name,
            icon_url=Interaction.user.avatar
        ))

    await poll.add_reaction('1️⃣')
    await poll.add_reaction('2️⃣')
    if option3 != None:
        await poll.add_reaction('3️⃣')
    if option4 != None:
        await poll.add_reaction('4️⃣')
    if option5 != None:
        await poll.add_reaction('5️⃣')
    if option6 != None:
        await poll.add_reaction('6️⃣')
    if option7 != None:
        await poll.add_reaction('7️⃣')
    if option8 != None:
        await poll.add_reaction('8️⃣')
    if option9 != None:
        await poll.add_reaction('9️⃣')
    if option10 != None:
        await poll.add_reaction('🔟')


@tree.command(
    name='whoreacted',
    description='Get a list of who reacted using what',
    guild=discord.Object(id=consts.GUILD))
async def self(Interaction: discord.Interaction, messageid: str, poll: bool):
    await Interaction.response.send_message('Gathering...')
    channel = Interaction.channel
    message = await Interaction.channel.fetch_message(int(messageid))
    users = list()
    for msgreaction in message.reactions:
        async for user in msgreaction.users():
            users.append(f'{str(msgreaction)} {str(user)}')
    users.sort()
    result = ''
    for user in users:
        if poll == True:
            if user.endswith('Bitey Frank#4533') == False:

                result += user+'\n'
        else:
            result += user+'\n'

    await channel.send(embed=discord.Embed(
        title='Who reacted to \"'+str(messageid)+'\"',
        description=result,
        color=discord.Color.green()
    ).set_author(
        name=Interaction.user.name,
        icon_url=Interaction.user.avatar))


@tree.command(
    name='polltotal',
    description='Get a tally of a poll',
    guild=discord.Object(id=consts.GUILD)
)
async def self(Interaction: discord.Interaction, messageid: str):
    await Interaction.response.send_message('Calculating...')
    message = await Interaction.channel.fetch_message(int(messageid))
    users = list()
    for msgreaction in message.reactions:
        async for user in msgreaction.users():
            thing = str(msgreaction)+' '+str(user)
            users.append(str(thing))

    users.sort()
    totalPollers = len(users)
    for user in users:
        if user.endswith('Bitey Frank#4533'):
            totalPollers -= 1
    onePollers = -1
    twoPollers = -1
    threePollers = -1
    fourPollers = -1
    fivePollers = -1
    sixPollers = -1
    sevenPollers = -1
    eightPollers = -1
    ninePollers = -1
    tenPollers = -1

    msg = f'Poll: {str(message.embeds[0].title)}\n\n{str(message.embeds[0].description)}\n\n\nTotal Pollers: {str(totalPollers)}\n\n'

    for user in users:
        if user.startswith('1️⃣') == True:
            onePollers += 1
        elif user.startswith('2️⃣') == True:
            twoPollers += 1
        elif user.startswith('3️⃣') == True:
            threePollers += 1
        elif user.startswith('4️⃣') == True:
            fourPollers += 1
        elif user.startswith('5️⃣') == True:
            fivePollers += 1
        elif user.startswith('6️⃣') == True:
            sixPollers += 1
        elif user.startswith('7️⃣') == True:
            sevenPollers += 1
        elif user.startswith('8️⃣') == True:
            eightPollers += 1
        elif user.startswith('9️⃣') == True:
            ninePollers += 1
        elif user.startswith('🔟') == True:
            tenPollers += 1

    onePollersPercentage = float(onePollers/totalPollers)

    msg += '1️⃣ *'+str(round(onePollersPercentage*100, 2)) + \
        '%* **('+str(onePollers)+')\n\n**'

    twoPollersPercentage = float(twoPollers/totalPollers)

    msg += '2️⃣ *'+str(round(twoPollersPercentage*100, 2)) + \
        '%* **('+str(twoPollers)+')\n\n**'

    if users.count('3️⃣') != 0:
        threePollersPercentage = float(threePollers/totalPollers)
        msg += '3️⃣ *'+str(round(threePollersPercentage*100, 2)) + \
            '%* **('+str(threePollers)+')\n\n**'

    if users.count('4️⃣') != 0:
        fourPollersPercentage = float(fourPollers/totalPollers)
        msg += '4️⃣ *'+str(round(fourPollersPercentage*100, 2)) + \
            '%* **('+str(fourPollers)+')\n\n**'

    if users.count('5️⃣') != 0:
        fivePollersPercentage = float(fivePollers/totalPollers)
        msg += '5️⃣ *'+str(round(fivePollersPercentage*100, 2)) + \
            '%* **('+str(fivePollers)+')\n\n**'

    if users.count('6️⃣') != 0:
        sixPollersPercentage = float(sixPollers/totalPollers)
        msg += '6️⃣ *'+str(round(sixPollersPercentage*100, 2)) + \
            '%* **('+str(sixPollers)+')\n\n**'

    if users.count('7️⃣') != 0:
        sevenPollersPercentage = float(sevenPollers/totalPollers)
        msg += '7️⃣ *'+str(round(sevenPollersPercentage*100, 2)) + \
            '%* **('+str(sevenPollers)+')\n\n**'

    if users.count('8️⃣') != 0:
        eightPollersPercentage = float(eightPollers/totalPollers)
        msg += '8️⃣ *'+str(round(eightPollersPercentage*100, 2)) + \
            '%* **('+str(eightPollers)+')\n\n**'

    if users.count('9️⃣') != 0:
        ninePollersPercentage = float(ninePollers/totalPollers)
        msg += '9️⃣ *'+str(round(ninePollersPercentage*100, 2)) + \
            '%* **('+str(ninePollers)+')\n\n**'

    if users.count('🔟') != 0:
        tenPollersPercentage = float(tenPollers/totalPollers)
        msg += '🔟 *'+str(round(tenPollersPercentage*100, 2)) + \
            '%* **('+str(tenPollers)+')\n\n**'

    await Interaction.channel.send(
        embed=discord.Embed(
            title='Tallied Votes',
            description=msg,
            color=discord.Color.green()
        ).set_author(
            name=Interaction.user.name,
            icon_url=Interaction.user.avatar
        ))


@tree.command(
    name='whowon',
    description='who won?',
    guild=discord.Object(id=consts.GUILD)
)
async def self(Interaction: discord.Interaction, magicdiepollid: str, doublenothingpollid: str, magicnumberasemoji: str, doublenumberasemoji: str):
    await Interaction.response.send_message('Gathering...')
    channel = Interaction.channel
    message = await Interaction.channel.fetch_message(int(magicdiepollid))
    Magicusers = list()
    for msgreaction in message.reactions:
        async for user in msgreaction.users():
            Magicusers.append(f'{str(msgreaction)} {str(user)}')
    Magicusers.sort()
    result = ''
    for user in Magicusers:
        if user.endswith('Bitey Frank#4533') == False:
            if user.startswith(magicnumberasemoji):
                result += user+'\n'

    await channel.send(embed=discord.Embed(
        title='Who Won?',
        description=result,
        color=discord.Color.green()
    ).set_author(
        name=Interaction.user.name,
        icon_url=Interaction.user.avatar))

    message = await Interaction.channel.fetch_message(int(doublenothingpollid))
    Doubleusers = list()
    for msgreaction in message.reactions:
        async for user in msgreaction.users():
            Doubleusers.append(f'{str(msgreaction)} {str(user)}')
    Doubleusers.sort()
    result = ''
    for user in Doubleusers:
        if user.endswith('Bitey Frank#4533') == False:
            if user.startswith(doublenumberasemoji):
                result += user+'\n'

    await channel.send(embed=discord.Embed(
        title='Who Won? (double)',
        description=result,
        color=discord.Color.green()
    ).set_author(
        name=Interaction.user.name,
        icon_url=Interaction.user.avatar))


@tree.command(
    name="reboot",
    description="Admin Only Command: Reboot Bitey Frank",
    guild=discord.Object(id=consts.GUILD)
)
async def self(Interaction: discord.Interaction):
    await Interaction.response.send_message("Rebooting...")
    sys.exit()


client.run(consts.TOKEN)
