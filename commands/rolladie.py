import functs
import discord
import random
from variables import dieEmojiMap

def import_command():
    # Command Info
    @functs.tree.command(
        name="rolladie",
        description="Roll a d6",
        guild=discord.Object(id=1030635475528056872)
    )
    # Code to Run Here
    async def self(Interaction:discord.Interaction):
        await Interaction.response.send_message(f'Rolled a {random.choice(dieEmojiMap)}')

