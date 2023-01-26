"""
Contains code for managing polls
"""
import discord
from discord import Interaction, Client, Message
from discord.app_commands import CommandTree
import consts


MIN_OPTIONS = 2
MAX_OPTIONS = 10
OPTION_EMOTES = [
    '1️⃣',
    '2️⃣',
    '3️⃣',
    '4️⃣',
    '5️⃣',
    '6️⃣',
    '7️⃣',
    '8️⃣',
    '9️⃣',
    '🔟',
]


def create_poll_commands(client: Client, tree: CommandTree):
    @tree.command(
        name='poll',
        description='Make a poll',
        guild=discord.Object(id=consts.GUILD)
    )
    async def make_poll(act: Interaction, question: str, *options: str):
        """Create a poll"""
        if not (MIN_OPTIONS <= len(options) <= MAX_OPTIONS):
            await act.response.send_message(
                f"Polls must have between {MIN_OPTIONS} and "
                f"{MAX_OPTIONS} options"
            )
            return
        if act.channel_id is None:
            await act.response.send_message("Poll must be in a channel")
            return

        reveal_type(act.channel_id)

        await act.response.send_message("Creating poll", ephemeral=True)

        description = ""
        for option, emote in zip(options, OPTION_EMOTES):
            description += f"{emote} {option}\n\n"

        poll = await client.get_channel(act.channel_id).send(
            embed=discord.Embed(
                title=question,
                description=description,
                color=discord.Color.green()
            ).set_author(
                name=act.user.name,
                icon_url=act.user.display_avatar
            )
        )

        for _, emote in zip(options, OPTION_EMOTES):
            await poll.add_reaction(emote)

    async def get_response_map(act: Interaction) -> tuple[dict[str, list[str]], int, Message]:
        """Return a mapping of responses"""

        # Get the parent message
        parent = act.message.reference

        if parent is None:
            raise ValueError("Message must be a reply")

        message = await act.channel.fetch_message(parent.message_id)

        # Map reactions to users
        response_map: dict[str, list[str]] = {}
        users: set[str] = set()

        for emote in message.reactions:
            async for user in emote.users():
                emote = str(emote)
                user = str(user)
                # Avoid duplicate votes, only count their first one
                if user not in users:
                    users.add(user)
                    response_map[emote] = response_map.get(emote, []) + [user]

        num_responses = len(users)
        for user in users:
            if user.endswith(consts.BOT_NAME):
                num_responses -= 1

        return response_map, num_responses, message

    @tree.command(
        name='whoreacted',
        description='Get a list of who reacted using what',
        guild=discord.Object(id=consts.GUILD))
    async def who_reacted(act: discord.Interaction):
        await act.response.send_message('Gathering...', ephemeral=True)

        response_map, _, message = await get_response_map(act)

        result = ''
        for emote, users in response_map.items():
            for u in users:
                result += f"{emote} {u}\n"

        await act.channel.send(embed=discord.Embed(
                title=f"Who reacted to {message.embeds[0].title}",
                description=result,
                color=discord.Color.green()
            ).set_author(
                name=act.user.name,
                icon_url=act.user.avatar
            )
        )

    @tree.command(
        name='polltotal',
        description='Get a tally of a poll',
        guild=discord.Object(id=consts.GUILD)
    )
    async def poll_total(act: Interaction):
        await act.response.send_message('Calculating...', ephemeral=True)

        response_map, num_responses, message = await get_response_map(act)

        response_msg = '\n'.join([
            f"Poll: {message.embeds[0].title}",
            "",
            f"{message.embeds[0].description}",
            "",
            "",
            f"Number of responses: {num_responses}",
            "",
            "",
        ])

        for emote, reactors in response_map:
            num = len(reactors)
            percent = round(num / num_responses * 100, 2)
            response_msg += f"{emote} *{percent}%* **({num})**\n\n"

        await act.channel.send(
            embed=discord.Embed(
                title='Tallied Votes',
                description=response_msg.strip(),
                color=discord.Color.green(),
            ).set_author(
                name=act.user.name,
                icon_url=act.user.display_avatar,
            )
        )

    @tree.command(
        name='whowon',
        description='who won?',
        guild=discord.Object(id=consts.GUILD)
    )
    async def who_won(act: Interaction, magic_number: str):
        await act.response.send_message('Calculating...', ephemeral=True)

        correct_react = OPTION_EMOTES[int(magic_number)]

        response_map, *_ = await get_response_map(act)

        result = '\n'.join(response_map[correct_react])

        await act.channel.send(embed=discord.Embed(
            title='Who Won?',
            description=result,
            color=discord.Color.green()
        ).set_author(
            name=act.user.name,
            icon_url=act.user.avatar)
        )
