"""
Contains code for managing roles
"""
import discord
from typing import Optional
from dataclasses import dataclass
from discord.ui import Button, View
from discord import Interaction
from consts import GUILD

@dataclass
class RoleInfo:
    """Contains information about a role"""

    name: str
    """Name of the role, to be used on the button"""
    emoji: str
    """Emoji for the role, to be used on the button too"""
    role: int
    """Role ID to use"""
    give_message: Optional[str] = None
    """Response to send when someone is given the role"""
    take_message: Optional[str] = None
    """Response to send when someone has the role taken from them"""


async def send_roles_callback(client, roles: list[RoleInfo], role_type: str):
    def generate_callback(info: RoleInfo):
        """Generate callback for button presses"""
        # Set up default give/take messages if required
        if info.give_message is None:
            info.give_message = f"Gave {info.name} role"
        if info.take_message is None:
            info.take_message = f"Removed {info.name} role"

        async def callback(interaction: Interaction):
            role = client.get_guild(GUILD).get_role(info.role)
            member = client.get_guild(GUILD).get_member(interaction.user.id)
            if member in role.members:
                role_mod = member.remove_roles(role)
                response = interaction.response.send_message(info.take_message, ephemeral=True)
            else:
                role_mod = member.add_roles(role)
                response = interaction.response.send_message(info.give_message, ephemeral=True)
            await role_mod
            await response
        return callback

    view = View()

    for role in roles:
        butt = Button(
            label=role.name, style=discord.ButtonStyle.gray, emoji=role.emoji)
        butt.callback = generate_callback(role)
        view.add_item(butt)

    await client.get_channel(1043016204278829066).send(f'Click a button to choose various *{role_type}*', view=view)
