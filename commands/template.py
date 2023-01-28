import functs
import discord


def import_command():
    # Command Info
    @functs.tree.command(
        name="Command Name (No Spaces/Caps/Special Characters)",
        description="Description here",
        guild=discord.Object(id=1030635475528056872)
    )
    # Code to Run Here
    async def self(Interaction:discord.Interaction):
        pass # delete this before you start coding