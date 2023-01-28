from dotenv import load_dotenv
from os import getenv

frankJoinEmotes =[
    '<:chonkfronk:1040418775129927752>',
    '<:frank3:1040422477433675857>',
    '<:sneakyfrank:1040419659792515213>',
    '<:hideyhole:1042217416278692003>',
    '<:jpeg:1042214971460829326>'
    ]

frankjpegs = []


numericEmojiMap={
    "1": "1️⃣",
    "2": "2️⃣",
    "3": "3️⃣",
    "4": "4️⃣",
    "5": "5️⃣"
}

dieEmojiMap={
    0: '<:die1:1068777948062175252>',
    1: '<:die2:1068777946522845215>',
    2: '<:die3:1068777944056610826>',
    3: '<:die4:1068777942743797871>',
    4: '<:die5:1068777941548400670>',
    5: '<:die6:1068777939036024862>'
}

load_dotenv()
TOKEN = getenv('DISCORD_TOKEN')
GUILD = getenv('DISCORD_GUILD')


