import functs
import variables
import random

def set_events():
    # Welcome users
    @functs.client.event
    async def on_member_join(member):
        await functs.client.get_channel(
            1030635476245286978
            ).send(
                random.choice(variables.frankJoinEmotes)
                )
        print(f'Greeted {str(member)}')
    # Say goodbye to users

    @functs.client.event
    async def on_member_remove(member):
        await functs.client.get_channel(
            1030635476245286978
            ).send(
                f"{member.mention} <:frank:1040418489476853872>7"
                )
        print(f'Said goodbye to {str(member)}')

    @functs.client.event
    async def on_message(message):
        for person in message.mentions:
            if person.id == 1045778486977118339:
                await functs.client.get_channel(message.channel.id).send(random.choice(variables.frankJoinEmotes))