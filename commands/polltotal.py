import functs
import discord

def import_command():
    @functs.tree.command(
        name='polltotal',
        description='Get a tally of a poll',
        guild=discord.Object(id=1030635475528056872)
        )
    async def self(Interaction:discord.Interaction,messageid:str):
        await Interaction.response.send_message('Calculating...')
        message=await Interaction.channel.fetch_message(int(messageid))
        users=list()
        for msgreaction in message.reactions:
            async for user in msgreaction.users():
                thing=str(msgreaction)+' '+str(user)
                users.append(str(thing))
        
        users.sort()
        totalPollers=len(users)
        for user in users:
            if user.endswith('Bitey Frank#4533'):
                totalPollers-=1
        onePollers=-1
        twoPollers=-1
        threePollers=-1
        fourPollers=-1
        fivePollers=-1
        sixPollers=-1
        sevenPollers=-1
        eightPollers=-1
        ninePollers=-1
        tenPollers=-1

        msg=f'Poll: {str(message.embeds[0].title)}\n\n{str(message.embeds[0].description)}\n\n\nTotal Pollers: {str(totalPollers)}\n\n'

        for user in users:
            if user.startswith('1️⃣') == True:
                onePollers+=1
            else:
                if user.startswith('2️⃣') == True:
                    twoPollers+=1
                else:
                    if user.startswith('3️⃣') == True:
                        threePollers+=1
                    else:
                        if user.startswith('4️⃣') == True:
                            fourPollers+=1
                        else:
                            if user.startswith('5️⃣') == True:
                                fivePollers+=1
                            else:
                                if user.startswith('6️⃣') == True:
                                    sixPollers+=1
                                else:
                                    if user.startswith('7️⃣') == True:
                                        sevenPollers+=1
                                    else:
                                        if user.startswith('8️⃣') == True:
                                            eightPollers+=1
                                        else:
                                            if user.startswith('9️⃣') == True:
                                                ninePollers+=1
                                            else:
                                                if user.startswith('🔟') == True:
                                                    tenPollers+=1


        


        onePollersPercentage=float(onePollers/totalPollers)

        msg+='1️⃣ *'+str(round(onePollersPercentage*100,2))+'%* **('+str(onePollers)+')\n\n**'

        twoPollersPercentage=float(twoPollers/totalPollers)

        msg+='2️⃣ *'+str(round(twoPollersPercentage*100,2))+'%* **('+str(twoPollers)+')\n\n**'

        if users.count('3️⃣') != 0:
            threePollersPercentage=float(threePollers/totalPollers)
            msg+='3️⃣ *'+str(round(threePollersPercentage*100,2))+'%* **('+str(threePollers)+')\n\n**'

        if users.count('4️⃣') != 0:
            fourPollersPercentage=float(fourPollers/totalPollers)
            msg+='4️⃣ *'+str(round(fourPollersPercentage*100,2))+'%* **('+str(fourPollers)+')\n\n**'

        if users.count('5️⃣') != 0:
            fivePollersPercentage=float(fivePollers/totalPollers)
            msg+='5️⃣ *'+str(round(fivePollersPercentage*100,2))+'%* **('+str(fivePollers)+')\n\n**'

        if users.count('6️⃣') != 0:
            sixPollersPercentage=float(sixPollers/totalPollers)
            msg+='6️⃣ *'+str(round(sixPollersPercentage*100,2))+'%* **('+str(sixPollers)+')\n\n**'

        if users.count('7️⃣') != 0:
            sevenPollersPercentage=float(sevenPollers/totalPollers)
            msg+='7️⃣ *'+str(round(sevenPollersPercentage*100,2))+'%* **('+str(sevenPollers)+')\n\n**'

        if users.count('8️⃣') != 0:
            eightPollersPercentage=float(eightPollers/totalPollers)
            msg+='8️⃣ *'+str(round(eightPollersPercentage*100,2))+'%* **('+str(eightPollers)+')\n\n**'

        if users.count('9️⃣') != 0:
            ninePollersPercentage=float(ninePollers/totalPollers)
            msg+='9️⃣ *'+str(round(ninePollersPercentage*100,2))+'%* **('+str(ninePollers)+')\n\n**'

        if users.count('🔟') != 0:
            tenPollersPercentage=float(tenPollers/totalPollers)
            msg+='🔟 *'+str(round(tenPollersPercentage*100,2))+'%* **('+str(tenPollers)+')\n\n**'

        await Interaction.channel.send(
            embed=discord.Embed(
                title='Tallied Votes',
                description=msg,
                color=discord.Color.green()
                ).set_author(
                    name=Interaction.user.name,
                    icon_url=Interaction.user.avatar
                ))
