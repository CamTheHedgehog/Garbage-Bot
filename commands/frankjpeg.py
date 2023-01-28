import functs
import variables
import discord

def import_command():
    @functs.tree.command(
        name='frankjpeg',
        description=f'Choose a specific frank .jpeg (out of 0 to {str(len(variables.frankjpegs)-1)})',
        guild=discord.Object(id=1030635475528056872)
        )
    async def self(Interaction:discord.Interaction, option: int):
        await Interaction.response.send_message(file=discord.File(variables.frankjpegs[option]))
        print('Ran /frankjpeg')