import functs
import discord

def import_command():
    @functs.tree.command(
        name='poll',
        description='Make a poll',
        guild=discord.Object(id=1030635475528056872))
    async def embed(Interaction:discord.Interaction, question:str, option1: str, option2: str, option3: str=None, option4: str=None, option5: str=None, option6: str=None, option7: str=None, option8: str=None, option9: str=None, option10: str=None):
        await Interaction.response.send_message('Creating Poll',ephemeral=True)
        description='1️⃣ '+option1+'\n\n2️⃣ '+option2

        if option3 != None:
            description+='\n\n3️⃣ '+option3
        if option4 != None:
            description+='\n\n4️⃣ '+option4
        if option5 != None:
            description+='\n\n5️⃣ '+option5
        if option6 != None:
            description+='\n\n6️⃣ '+option6
        if option7 != None:
            description+='\n\n7️⃣ '+option7
        if option8 != None:
            description+='\n\n8️⃣ '+option8
        if option9 != None:
            description+='\n\n9️⃣ '+option9
        if option10 != None:
            description+='\n\n🔟 '+option10
        
        poll= await functs.client.get_channel(Interaction.channel_id).send(
            embed=discord.Embed(
                title=question,
                description=description,
                color=discord.Color.green()
                ).set_author(
                    name=Interaction.user.name,
                    icon_url=Interaction.user.avatar
                ))

        await poll.add_reaction('1️⃣')
        await poll.add_reaction('2️⃣')
        if option3 != None:
            await poll.add_reaction('3️⃣')
        if option4 != None:
            await poll.add_reaction('4️⃣')
        if option5 != None:
            await poll.add_reaction('5️⃣')
        if option6 != None:
            await poll.add_reaction('6️⃣')
        if option7 != None:
            await poll.add_reaction('7️⃣')
        if option8 != None:
            await poll.add_reaction('8️⃣')
        if option9 != None:
            await poll.add_reaction('9️⃣')
        if option10 != None:
            await poll.add_reaction('🔟')