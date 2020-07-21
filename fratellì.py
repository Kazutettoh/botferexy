#By github.com/CometaLunare  #all rights reserved

import asyncio
from telethon import events
from userbot import bot
from userbot.system import dev_cmd

@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.4

    animation_ttl = range(0, 117)

    input_str = event.pattern_match.group(1)

    if input_str == "muro":

        await event.edit(input_str)

        animation_chars = [
            
            
"||                  🚙",
"Na piotta e 10,",
"Na piotta e 10, 3ª MARCIA",

"||                🚙",

"||               🚙",

"||              🚙",

             "Quando il semaforo è rosso🟢",

"Quando il semaforo è rosso🟡",

"Quando il semaforo è rosso🔴",

"||            🚙",

"||           🚙",



"Si fa così!😳",

"Imbocchi qua,",

"Imbocchi qua, gliela giri qua,",

"Imbocchi qua, gliela giri qua, fratellì così!",

"|| 🚙",

"||🚙",

"|🚙",



"Doveva annà così fratellì,"

"Ho preso il muro fratellì♿️💤"








                            

        ]


        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 117])

