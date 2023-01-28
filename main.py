import variables
import functs
from commands import *
from events import set_events
import os
from variables import frankjpegs
from functs import client

for frankJpeg in os.listdir('beajpeg-assets'):
    if frankJpeg.endswith(('jpg','jpeg','png','webp','gif')):
        frankjpegs.append(f'beajpeg-assets/{frankJpeg}')
    else:
        client.get_channel(
            '1061732002275016745'
            ).send(
                f'Warning, file \"{frankJpeg}\" is not a supported Frank JPEG'
                )
        
for command in os.listdir('commands'):
    if command.endswith('py'):
        if command.endswith('__init__.py') == False:
            if command.endswith('template.py') == False:
                exec(f'{command[:-3]}.import_command()')

set_events()

functs.client.run(variables.TOKEN)
