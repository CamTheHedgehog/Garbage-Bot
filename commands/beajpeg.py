import functs
import discord
import random
import variables

def import_command():
    @functs.tree.command(
        name="beajpeg",
        description="Make frank be a .jpeg",
        guild=discord.Object(id=1030635475528056872)
        )
    async def self(Interaction:discord.Interaction):
        await Interaction.response.send_message(file=discord.File(random.choice(variables.frankjpegs)))
        print('Ran /beajpeg')