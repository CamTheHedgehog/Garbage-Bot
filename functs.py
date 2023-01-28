import os
import discord
from discord.ui import Button, View
import time
from discord import app_commands

intents = discord.Intents.default()
intents.members = True

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)

    async def on_ready(self):
        await self.wait_until_ready()
        self.synced = False
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=1030635475528056872))
            self.synced=True
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
tree = app_commands.CommandTree(client)


# Definitions

async def sendButtonPingRoles():
    GeneralAnnouncements=Button(
        label="General Announcements",
        style=discord.ButtonStyle.gray,
        emoji="🔔"
        )
    DankPods=Button(
        label="DankPods",
        style=discord.ButtonStyle.gray,
        emoji="<:dankpods:1040417450686173184>"
        )
    GarbageTime=Button(
        label="Garbage Time",
        style=discord.ButtonStyle.gray,
        emoji="<:tony:1040419706399625266>"
        )
    MornGarbageStream=Button(
        label="Garbage Stream (Morn)",
        style=discord.ButtonStyle.gray,
        emoji="<:chonkfronk:1040418775129927752>"
        )
    ArvoGarbageStream=Button(
        label="Garbage Stream (Arvo)",
        style=discord.ButtonStyle.gray,
        emoji="<:shrek:1040482904414879826>"
        )
    TheDrumThing=Button(
        label="The Drum Thing",
        style=discord.ButtonStyle.gray,
        emoji="<:drumthing:1041177501604515960>"
        )
    Polls=Button(
        label="Polls",
        style=discord.ButtonStyle.gray,
        emoji="📊"
        )

# General Announcement Ping (1043020516346302504)
    async def GeneralAnnouncementsCallback(button_info):
        role = client.get_guild(1030635475528056872).get_role(1043020516346302504)
        member = client.get_guild(1030635475528056872).get_member(button_info.user.id)

        if role.members.__contains__(member):
            await member.remove_roles(role)
            await button_info.response.send_message("Removed \"General Announcement Ping\" Role", ephemeral=True)
        else:
            await member.add_roles(role)
            await button_info.response.send_message("You have been given the \"General Announcement Ping\" Role", ephemeral=True)
# DankPods Ping (1043016550103384064)
    async def DankPodsCallback(button_info):
        role = client.get_guild(1030635475528056872).get_role(1043016550103384064)
        member = client.get_guild(1030635475528056872).get_member(button_info.user.id)

        if role.members.__contains__(member):
            await member.remove_roles(role)
            await button_info.response.send_message("Removed \"DankPods Ping\" Role", ephemeral=True)
        else:
            await member.add_roles(role)
            await button_info.response.send_message("You have been given the \"DankPods Ping\" Role", ephemeral=True)
# Garbage Time Ping (1043016644412317776)
    async def GarbageTimeCallback(button_info):
        role = client.get_guild(1030635475528056872).get_role(1043016644412317776)
        member = client.get_guild(1030635475528056872).get_member(button_info.user.id)

        if role.members.__contains__(member):
            await member.remove_roles(role)
            await button_info.response.send_message("Removed \"Garbage Time Ping\" Role", ephemeral=True)
        else:
            await member.add_roles(role)
            await button_info.response.send_message("You have been given the \"Garbage Time Ping\" Role", ephemeral=True)
# Garbage Stream Morn Ping (1043016713677053982)
    async def MornGarbageStreamCallback(button_info):
        role = client.get_guild(1030635475528056872).get_role(1043016713677053982)
        member = client.get_guild(1030635475528056872).get_member(button_info.user.id)

        if role.members.__contains__(member):
            await member.remove_roles(role)
            await button_info.response.send_message("Removed \"Garbage Stream Morn Ping\" Role", ephemeral=True)
        else:
            await member.add_roles(role)
            await button_info.response.send_message("You have been given the \"Garbage Stream Morn Ping\" Role", ephemeral=True)
# Garbage Stream Arvo Ping (1043020552878702612)
    async def ArvoGarbageStreamCallback(button_info):
        role = client.get_guild(1030635475528056872).get_role(1043020552878702612)
        member = client.get_guild(1030635475528056872).get_member(button_info.user.id)

        if role.members.__contains__(member):
            await member.remove_roles(role)
            await button_info.response.send_message("Removed \"Garbage Stream Arvo Ping\" Role", ephemeral=True)
        else:
            await member.add_roles(role)
            await button_info.response.send_message("You have been given the \"Garbage Stream Arvo Ping\" Role", ephemeral=True)
# The Drum Thing Ping (1043016786100101240)
    async def TheDrumThingCallback(button_info):
        role = client.get_guild(1030635475528056872).get_role(1043016786100101240)
        member = client.get_guild(1030635475528056872).get_member(button_info.user.id)

        if role.members.__contains__(member):
            await member.remove_roles(role)
            await button_info.response.send_message("Removed \"The Drum Thing Ping\" Role", ephemeral=True)
        else:
            await member.add_roles(role)
            await button_info.response.send_message("You have been given the \"The Drum Thing Ping\" Role", ephemeral=True)
# Poll Ping (1044037090066833508)
    async def PollsCallback(button_info):
        role = client.get_guild(1030635475528056872).get_role(1044037090066833508)
        member = client.get_guild(1030635475528056872).get_member(button_info.user.id)

        if role.members.__contains__(member):
            await member.remove_roles(role)
            await button_info.response.send_message("Removed \"Poll Ping\" Role", ephemeral=True)
        else:
            await member.add_roles(role)
            await button_info.response.send_message("You have been given the \"Poll Ping\" Role", ephemeral=True)

    GeneralAnnouncements.callback=GeneralAnnouncementsCallback
    DankPods.callback=DankPodsCallback
    GarbageTime.callback=GarbageTimeCallback
    MornGarbageStream.callback=MornGarbageStreamCallback
    ArvoGarbageStream.callback=ArvoGarbageStreamCallback
    TheDrumThing.callback=TheDrumThingCallback
    Polls.callback=PollsCallback
        
    view=View(timeout=None)
    view.add_item(GeneralAnnouncements)
    view.add_item(DankPods)
    view.add_item(GarbageTime)
    view.add_item(MornGarbageStream)
    view.add_item(ArvoGarbageStream)
    view.add_item(TheDrumThing)
    view.add_item(Polls)
    await client.get_channel(1043016204278829066).send('Click a button to choose various *Ping Roles*', view=view)
async def sendButtonTonaRoles():
    OGTona=Button(
        label="OG Tona",
        style=discord.ButtonStyle.gray,
        emoji="<:tonatime:1040858187592642622>"
        )
    SkyHihi=Button(
        label="Sky Hihi",
        style=discord.ButtonStyle.gray,
        emoji="☁️"
        )
    RolloFinito=Button(
        label="Rollo Finito",
        style=discord.ButtonStyle.gray,
        emoji="🏁"
        )

# OG Tona (1043018409560002580)
    async def OGTonaCallback(button_info):
        role = client.get_guild(1030635475528056872).get_role(1043018409560002580)
        member = client.get_guild(1030635475528056872).get_member(button_info.user.id)

        if role.members.__contains__(member):
            await member.remove_roles(role)
            await button_info.response.send_message("Removed \"OG Tona\" Role", ephemeral=True)
        else:
            await member.add_roles(role)
            await button_info.response.send_message("You have been given the \"OG Tona\" Role", ephemeral=True)
# Sky Hihi (1043018486823272448)
    async def SkyHihiCallback(button_info):
        role = client.get_guild(1030635475528056872).get_role(1043018486823272448)
        member = client.get_guild(1030635475528056872).get_member(button_info.user.id)

        if role.members.__contains__(member):
            await member.remove_roles(role)
            await button_info.response.send_message("Removed \"Sky Hihi\" Role", ephemeral=True)
        else:
            await member.add_roles(role)
            await button_info.response.send_message("You have been given the \"Sky Hihi\" Role", ephemeral=True)
# Rollo Finito (1043018524324540478)
    async def RolloFinitoCallback(button_info):
        role = client.get_guild(1030635475528056872).get_role(1043018524324540478)
        member = client.get_guild(1030635475528056872).get_member(button_info.user.id)

        if role.members.__contains__(member):
            await member.remove_roles(role)
            await button_info.response.send_message("Removed \"Rollo Finito\" Role", ephemeral=True)
        else:
            await member.add_roles(role)
            await button_info.response.send_message("You have been given the \"Rollo Finito\" Role", ephemeral=True)

    OGTona.callback=OGTonaCallback
    SkyHihi.callback=SkyHihiCallback
    RolloFinito.callback=RolloFinitoCallback
    
    view=View(timeout=None)
    view.add_item(OGTona)
    view.add_item(SkyHihi)
    view.add_item(RolloFinito)

    await client.get_channel(1043016204278829066).send('Click a button to choose various *Tona Roles*', view=view)
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

#     async def timezoneCallback(interaction):
#         if select.values == True:
#             if select.values[0] == "GMT-12:00":
#                 role = variables.client.get_guild(1030635475528056872).get_role(1045189927954026537)
#             else:
#                 if select.values[0] == "GMT-11:00":
#                     role = variables.client.get_guild(1030635475528056872).get_role(1045189924883808278)
#                 else:
#                     if select.values[0] == "GMT-10:00":
#                         role = variables.client.get_guild(1030635475528056872).get_role(1045189921905848320)
#                     else:
#                         if select.values[0] == "GMT-9:00":
#                             role = variables.client.get_guild(1030635475528056872).get_role(1045189918806261810)
#                         else:
#                             if select.values[0] == "GMT-8:00":
#                                 role = variables.client.get_guild(1030635475528056872).get_role(1045189915257872444)
#                             else:
#                                 if select.values[0] == "GMT-7:00":
#                                     role = variables.client.get_guild(1030635475528056872).get_role(1045189909733974026)
#                                 else:
#                                     if select.values[0] == "GMT-6:00":
#                                         role = variables.client.get_guild(1030635475528056872).get_role(1045189905971679283)
#                                     else:
#                                         if select.values[0] == "GMT-5:00":
#                                             role = variables.client.get_guild(1030635475528056872).get_role(1045189901970313219)
#                                         else:
#                                             if select.values[0] == "GMT-4:00":
#                                                 role = variables.client.get_guild(1030635475528056872).get_role(1045189897004257291)
#                                             else:
#                                                 if select.values[0] == "GMT-3:00":
#                                                     role = variables.client.get_guild(1030635475528056872).get_role(1045189725679534101)
#                                                 else:
#                                                     if select.values[0] == "GMT-2:00":
#                                                         role = variables.client.get_guild(1030635475528056872).get_role(1045189620712865882)
#                                                     else:
#                                                         if select.values[0] == "GMT-1:00":
#                                                             role = variables.client.get_guild(1030635475528056872).get_role(1045188897325461554)
#                                                         else:
#                                                             if select.values[0] == "GMT±0:00":
#                                                                 role = variables.client.get_guild(1030635475528056872).get_role(1045186821384065045)
#                                                             else:
#                                                                 if select.values[0] == "GMT+1:00":
#                                                                     role = variables.client.get_guild(1030635475528056872).get_role(1045190313519616050)
#                                                                 else:
#                                                                     if select.values[0] == "GMT+2:00":
#                                                                         role = variables.client.get_guild(1030635475528056872).get_role(1045190317550354442)
#                                                                     else:
#                                                                         if select.values[0] == "GMT+3:00":
#                                                                             role = variables.client.get_guild(1030635475528056872).get_role(1045190325699891240)
#                                                                         else:
#                                                                             if select.values[0] == "GMT+3:30":
#                                                                                 role = variables.client.get_guild(1030635475528056872).get_role(1045196700156952628)
#                                                                             else:
#                                                                                 if select.values[0] == "GMT+4:00":
#                                                                                     role = variables.client.get_guild(1030635475528056872).get_role(1045190328703000596)
#                                                                                 else:
#                                                                                     if select.values[0] == "GMT+4:30":
#                                                                                         role = variables.client.get_guild(1030635475528056872).get_role(1045196824501309481)
#                                                                                     else:
#                                                                                         if select.values[0] == "GMT+5:00":
#                                                                                             role = variables.client.get_guild(1030635475528056872).get_role(1045190332041678959)
#                                                                                         else:
#                                                                                             if select.values[0] == "GMT+5:30":
#                                                                                                 role = variables.client.get_guild(1030635475528056872).get_role(1045196973822726246)
#                                                                                             else:
#                                                                                                 if select.values[0] == "GMT+6:00":
#                                                                                                     role = variables.client.get_guild(1030635475528056872).get_role(1045190335971721237)
#                                                                                                 else:
#                                                                                                     if select.values[0] == "GMT+6:30":
#                                                                                                         role = variables.client.get_guild(1030635475528056872).get_role(1045197080844578866)
#                                                                                                     else:
#                                                                                                         if select.values[0] == "GMT+7:00":
#                                                                                                             role = variables.client.get_guild(1030635475528056872).get_role(1045190339163594812)
#                                                                                                         else:
#                                                                                                             if select.values[0] == "GMT+8:00":
#                                                                                                                 role = variables.client.get_guild(1030635475528056872).get_role(1045190342351257691)
#                                                                                                             else:
#                                                                                                                 if select2.values[0] == "GMT+9:00":
#                                                                                                                     role = variables.client.get_guild(1030635475528056872).get_role(1045190345157246997)
#                                                                                                                 else:
#                                                                                                                     if select2.values[0] == "GMT+9:30":
#                                                                                                                         role = variables.client.get_guild(1030635475528056872).get_role(1045197227041226762)
#                                                                                                                     else:
#                                                                                                                         if select2.values[0] == "GMT+10:00":
#                                                                                                                             role = variables.client.get_guild(1030635475528056872).get_role(1045190348437196851)
#                                                                                                                         else:
#                                                                                                                             if select2.values[0] == "GMT+10:30":
#                                                                                                                                 role = variables.client.get_guild(1030635475528056872).get_role(1045197320888787005)
#                                                                                                                             else:
#                                                                                                                                 if select2.values[0] == "GMT+11:00":
#                                                                                                                                     role = variables.client.get_guild(1030635475528056872).get_role(1045190353474555914)
#                                                                                                                                 else:
#                                                                                                                                     if select2.values[0] == "GMT+12:00":
#                                                                                                                                         role = variables.client.get_guild(1030635475528056872).get_role(1045190356741935145)
#                                                                                                                                     else:
#                                                                                                                                         if select2.values[0] == "GMT+13:00":
#                                                                                                                                             role = variables.client.get_guild(1030635475528056872).get_role(1045190359870869634)
#                                                                                                                                         else:
#                                                                                                                                             if select2.values[0] == "GMT+14:00":
#                                                                                                                                                 role = variables.client.get_guild(1030635475528056872).get_role(1045190363889016864)

#             member = variables.client.get_guild(1030635475528056872).get_member(interaction.user.id)
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
#     await variables.client.get_channel(1043016204278829066).send(content='Select the Option for your respective *Time Zone*',embed=discord.Embed(title='Time Zone Help', description='Calculate the amount of hours since Jan 1st 1970\n\n<t:0>', color=discord.Color.green()),view=view)


# Activate Bot

