import functs
import discord
import variables

def import_command():
    @functs.tree.command(
        name='listfrankjpegs',
        description='List the Frank .jpegs',
        guild=discord.Object(id=1030635475528056872)
        )
    async def self(Interaction:discord.Interaction):
        message='Frank jpegs:'
        id=0
        for jpegName in variables.frankjpegs:
            message+=f'\n*{str(id)}*: **__{jpegName[15:]}__**'
            id+=1
        await Interaction.response.send_message(message)
        print('Ran /listvariables.frankjpegs')