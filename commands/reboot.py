import functs
import discord
import sys

def import_command():
    @functs.tree.command(
        name="reboot",
        description="Admin Only Command: Reboot Bitey Frank",
        guild=discord.Object(id=1030635475528056872)
    )
    async def self(Interaction:discord.Interaction):
        await Interaction.response.send_message("Rebooting...")
        sys.exit()