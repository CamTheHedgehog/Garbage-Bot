"""
Contains constants used within the code
"""
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN: str = os.getenv('DISCORD_TOKEN')  # type: ignore
GUILD: str = os.getenv('DISCORD_GUILD')  # type: ignore
BOT_NAME = 'Bitey Frank#4533'

FRANK_JOIN_EMOTES = [
    '<:chonkfronk:1040418775129927752>',
    '<:frank3:1040422477433675857>',
    '<:sneakyfrank:1040419659792515213>',
    '<:hideyhole:1042217416278692003>',
    '<:jpeg:1042214971460829326>'
]
