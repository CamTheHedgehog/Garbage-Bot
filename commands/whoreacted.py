import functs
import discord

def import_command():
    @functs.tree.command(
        name='whoreacted',
        description='Get a list of who reacted using what',
        guild=discord.Object(id=1030635475528056872))
    async def self(Interaction:discord.Interaction, messageid:str, poll:bool):
        await Interaction.response.send_message('Gathering...')
        channel=Interaction.channel
        message=await Interaction.channel.fetch_message(int(messageid))
        users=list()
        for msgreaction in message.reactions:
            async for user in msgreaction.users():
                users.append(f'{str(msgreaction)} {str(user)}')
        users.sort()
        result=''
        for user in users:
            if poll==True:
                if user.endswith('Bitey Frank#4533') == False:

                    result+=user+'\n'
            else:
                result+=user+'\n'

        await channel.send(embed=discord.Embed(
            title='Who reacted to \"'+str(messageid)+'\"',
            description=result,
            color=discord.Color.green()
            ).set_author(
                name=Interaction.user.name,
                icon_url=Interaction.user.avatar))