import functs
import discord
import variables    

def import_command():
    @functs.tree.command(
        name='whowon',
        description='who won?',
        guild=discord.Object(id=1030635475528056872)
    )
    async def self(Interaction:discord.Interaction,magicdiepollid:str,doublenothingpollid:str,magicnumber:int,doublenumber:int):
        await Interaction.response.send_message('Gathering...')
        channel=Interaction.channel
        message=await Interaction.channel.fetch_message(int(magicdiepollid))
        Magicusers=list()
        for msgreaction in message.reactions:
            async for user in msgreaction.users():
                Magicusers.append(f'{str(msgreaction)} {str(user)}')
        Magicusers.sort()
        result=''
        if magicnumber > 0:
            if len(Magicusers) > 0:
                for user in Magicusers:
                        if user.endswith('Bitey Frank#4533') == False:
                            if user.startswith(variables.numericEmojiMap[str(magicnumber)]):
                                result+=user+'\n'
            else:
                result='Nobody'
        else:
            result='Nobody'

        await channel.send(embed=discord.Embed(
            title='Who Won?',
            description=result,
            color=discord.Color.green()
            ).set_author(
                name=Interaction.user.name,
                icon_url=Interaction.user.avatar))

        message=await Interaction.channel.fetch_message(int(doublenothingpollid))
        Doubleusers=list()
        for msgreaction in message.reactions:
            async for user in msgreaction.users():
                Doubleusers.append(f'{str(msgreaction)} {str(user)}')
        Doubleusers.sort()
        result=''
        if doublenumber > 0:
            if len(Doubleusers) > 0:
                for user in Doubleusers:
                        if user.endswith('Bitey Frank#4533') == False:
                            if user.startswith(variables.numericEmojiMap[str(doublenumber)]):
                                result+=user+'\n'
            else:
                result='Nobody'
        else:
            result='Nobody'

        await channel.send(embed=discord.Embed(
            title='Who Won? (double)',
            description=result,
            color=discord.Color.green()
            ).set_author(
                name=Interaction.user.name,
                icon_url=Interaction.user.avatar))