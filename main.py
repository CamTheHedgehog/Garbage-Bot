import os
import discord
import random
import time
from discord import app_commands
import sys
import consts
from role_management import RoleInfo, send_roles_callback
from poll_management import create_poll_commands


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

        ### CONTRIBUTORS, If you see this would you be able to make this loop every 10 minutes? ###
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
            1061732002275016745
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
async def be_a_jpeg(Interaction: discord.Interaction):
    await Interaction.response.send_message(file=discord.File(random.choice(frank_jpegs)))
    print('Ran /beajpeg')


@tree.command(
    name='frankjpeg',
    description=f'Choose a specific frank .jpeg (out of 0 to {str(len(frank_jpegs)-1)})',
    guild=discord.Object(id=consts.GUILD)
)
async def frank_jpeg(Interaction: discord.Interaction, option: int):
    await Interaction.response.send_message(file=discord.File(frank_jpegs[option]))
    print('Ran /frankjpeg')


@tree.command(
    name='listfrankjpegs',
    description='List the Frank .jpegs',
    guild=discord.Object(id=consts.GUILD)
)
async def list_frank_jpegs(Interaction: discord.Interaction):
    message = 'Frank jpegs:'
    id = 0
    for jpegName in frank_jpegs:
        message += f'\n*{str(id)}*: **__{jpegName[15:]}__**'
        id += 1
    await Interaction.response.send_message(message)
    print('Ran /listfrankjpegs')


# Polling
create_poll_commands(client, tree)


@tree.command(
    name="reboot",
    description="Admin Only Command: Reboot Bitey Frank",
    guild=discord.Object(id=consts.GUILD)
)
async def reboot(Interaction: discord.Interaction):
    await Interaction.response.send_message("Rebooting...")
    sys.exit()


client.run(consts.TOKEN)
