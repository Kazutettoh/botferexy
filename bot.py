import asyncio
from userbot import bot
from userbot.system import register
from telethon.tl.functions.account import UpdateProfileRequest
from telethon import events
from telethon.events import StopPropagation
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.functions.messages import ReportSpamRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon import functions, types
from telethon.tl.functions.messages import GetAllChatsRequest
from telethon.tl.functions.messages import GetAllChatsRequest


message = "**⛔️ Al momento sono OFFLINE.\n⚠️ Scrivi tutto in un messaggio e leggerò il prima possibile!**"
mexScuola = "**⛔️ Al momento sono OFFLINE.\n⚠️ Scrivi tutto in un messaggio e leggerò il prima possibile!.**"
exempt = []
mutedList = []
autoNiceText = False

# MUTE

@register(outgoing=True, pattern="^.mute$")
async def setMute(e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    if e.is_private and not (await e.get_sender()).bot:
      global mutedList
      if e.chat_id in mutedList:
        mutedList.remove(e.chat_id)
        await e.edit("`Sei stato smutato! Ora potrai scrivere!`")
      else:
        mutedList.append(e.chat_id)
        await e.edit("`Sei stato mutato! Qualsiasi messaggio verrà scritto sarà cancellato!`")
        
# ID

@register(outgoing=True, pattern="^.id")
async def getId(e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    if e.is_reply:
      try:
        reply = await e.get_reply_message()
        if reply.sender.username != None:
          await e.edit(f"**🆔 @{reply.sender.username}:** `{reply.sender.id}`")
        else:
          await e.edit(f"🆔 [{reply.sender.first_name}](tg://user?id={reply.sender.id})**:** `{reply.sender.id}`")
      except:
        await e.edit("**Entità non trovata. Riprova senza usare la @**")
    else:
      try:
        text = e.text.split(" ", 1)
        entity = await e.client.get_entity(text[1])
        if hasattr(entity, 'title'):
          await e.edit(f"**🆔 {entity.title}:** `{entity.id}`")
        else:
          if entity.username != None:
            await e.edit(f"**🆔 @{entity.username}:** `{entity.id}`")
          else:
            await e.edit(f"🆔 [{entity.firstname}](tg://user?id={entity.id})**:** `{entity.id}`")
      except:
        await e.edit("**Entità non trovata. Riprova senza usare la @**")
        
# COMANDI PERSONALI

@register(outgoing=True, pattern="^spadawdwadadw$")
async def Channels(e):
  await e.edit("https://t.me/joinchat/AAAAAFN-hR0DUWuCTP_Y2w LINK PER ENTRARE NEL CANALE DOVE ORGANIZZEREMO I SERVER PRIVATI.\nLE PASSWORD VARIE VERRANNO DATE QUI: https://t.me/joinchat/EcrJhhXAd5o0AVhQjt8FHA")
  
@register(outgoing=True, pattern="^.pula$")
async def CARABINIERIIIIIIIIIII(e):
  for i in range(10):
    await asyncio.wait([e.edit("🔵🔵🔵🔵   🔴🔴🔴🔴\n🔵🔵🔵🔵   🔴🔴🔴🔴\n🔵🔵🔵🔵   🔴🔴🔴🔴\n🔵🔵🔵🔵   🔴🔴🔴🔴")])
    await asyncio.sleep(0.1)
    await asyncio.wait([e.edit("🔴🔴🔴🔴   🔵🔵🔵🔵\n🔴🔴🔴🔴   🔵🔵🔵🔵\n🔴🔴🔴🔴   🔵🔵🔵🔵\n🔴🔴🔴🔴   🔵🔵🔵🔵")])
    await asyncio.sleep(0.1)
  await asyncio.wait([e.edit("**🚨🚔 CHIAMATE IL CIENTODICIOTTOOOOO!!! 🚔🚨**")])
  
@register(outgoing=True, pattern="^.fick$")
async def CARABINIERIIIIIIIIIII(e):
  for i in range(10):
    await asyncio.wait([e.edit("👉 👌")])
    await asyncio.sleep(0.1)
    await asyncio.wait([e.edit("👌 👉")])
    await asyncio.sleep(0.1)
    await asyncio.wait([e.edit("👌 👉")])
    await asyncio.sleep(0.1)
  await asyncio.wait([e.edit("**yes baby :)**")])

# OFFLINE / ONLINE
          
@register(outgoing=True, pattern="^.mex")
async def setMessage(e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    global message
    message = str(e.text[5:])
    await e.edit("`Messaggio impostato correttamente!`")

@register(outgoing=True, pattern="^.off$")
async def changeName(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        name = "Userbot 79 [𝔬𝔣𝔣𝔩𝔦𝔫𝔢]"
        await bot(UpdateProfileRequest(first_name=name, last_name=""))
        global message
        message = "**⛔️ Al momento sono OFFLINE.\n⚠️ Scrivi tutto in un messaggio e leggerò il prima possibile!.**"
        await e.edit("`Ora sei Offline`")
        
@register(outgoing=True, pattern="^.on$")
async def changeName(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        name = "Userbot 79 [𝑜𝓃𝓁𝒾𝓃𝑒]"
        await bot(UpdateProfileRequest(first_name=name, last_name=""))
        global message
        message = "**⛔️ Al momento sono OFFLINE.\n⚠️ Scrivi tutto in un messaggio e leggerò il prima possibile!.**"
        await e.edit("`Ora sei Online`")

@register(outgoing=True, pattern="^.mc$")
async def changeName(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        name = "Userbot 79 [sono su minecraft]"
        await bot(UpdateProfileRequest(first_name=name, last_name=""))
        global message
        message = "**⛔️ Al momento sono Minecraft se vuoi giocare con me .\n⚠️ aggiungimi agli amici di hypixel zferexy .**"
        await e.edit("`Ora sei su Minecraft`")

@register(outgoing=True, pattern="^.onplugin$")
async def changeName(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        name = "Userbot 79 [is creating plugin]"
        await bot(UpdateProfileRequest(first_name=name, last_name=""))
        global message
        message = "**⛔️ Al momento sto creando qualche plugin attendi qualche minuto.\n⚠️ rispondo in breve tempo.**"
        await e.edit("`Ora stai creando plugin`")
#Verify
verify = None
 
@register(outgoing=True, pattern="^[.]verify$")
async def Verify(e):
  global verify
  verify = e
  await e.client.send_message("@SpamBot", "/start")
 
@register(incoming=True)
async def checkVerify(e):
  global verify
  if verify != None:
    if e.chat_id == 178220800:
      if ":" in e.text:
        st = e.text.split(" ")
        for i in range(st.__len__()):
          if ":" in st[i]:
            fine = st[i - 3] + " " + st[i - 2] + " " + st[i - 1] + " Ore: " +st[i]
            break
        await verify.edit(f"**❌ Sei limitato fino al {fine} ❌**")
        verify = None
        await e.client(functions.messages.DeleteHistoryRequest(e.chat_id, 0, False, True))
      else:
        await verify.edit("**✅ Non sei limitato ✅**")
        verify = None
        await e.client(functions.messages.DeleteHistoryRequest(e.chat_id, 0, False, True))

#BLOCK
blockMessage = "**Ops, sei stato bloccato🤡♿️🔒**"

@register(outgoing=True, pattern="^[.]block$")
async def blockUser(e):
  if not (await e.get_sender()).bot:
    global blockMessage
    if e.is_reply:
      reply = await e.get_reply_message()
      await e.delete()
      await e.client.send_message(reply.chat_id, blockMessage, reply_to=reply)
      await e.client(BlockRequest(reply.sender.id))
    else:
      if e.is_private:
        await e.edit(blockMessage)
        await e.client(BlockRequest(e.chat_id))

unblockMessage = "**✅SEI STATO SBLOCCATO✅**"
 
@register(outgoing=True, pattern="^.unblock$")
async def unblockUser(e):
  if not e.text[0].isalpha():
    if not (await e.get_sender()).bot:
      global unblockMessage
      if e.is_reply:
        reply = await e.get_reply_message()
        await e.delete()
        await e.client.send_message(reply.chat_id, unblockMessage, reply_to=reply)
        await e.client(UnblockRequest(reply.sender.id))
      else:
        if e.is_private:
          await e.edit(unblockMessage)
          await e.client(UnblockRequest(e.chat_id))

# NICETEXT

@register(outgoing=True, pattern="^.niceText$")
async def setNiceText(e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    global autoNiceText
    if autoNiceText:
      autoNiceText = False
      await e.edit("`Animazione Testo Disattivata!`")
    else:
      autoNiceText = True
      await e.edit("`Animazione Testo Attivata!`")
#BTC
@register(outgoing=True, pattern="^[.]btc$")
async def bitCoinezzss(e):
  await e.edit("**Prezzo: " + str(requests.get("https://blockchain.info/ticker").json()["USD"]["last"]) + " USD**")
  
@register(outgoing=True, pattern="^[.]btceur$")
async def bitCoinezzss(e):
  await e.edit("**Prezzo: " + str(requests.get("https://blockchain.info/ticker").json()["EUR"]["last"]) + " EUR**")
      
@register(outgoing=True)
async def niceText(e):
  if e.text[0].isalpha() and not e.text == "Canali":
    global autoNiceText
    if autoNiceText:
      mex = ""
      for i in range(len(e.text)):
        if e.text[i] == " ":
          mex = mex + ' '
        else:
          mex = mex + e.text[i]
        await asyncio.wait([e.edit("`" + mex + " |`")])
        await asyncio.sleep(0.1)
        await asyncio.wait([e.edit("`" + mex + "  ‏‏‎ `")])
        await asyncio.sleep(0.1)
        if i == len(e.text) - 1:
          await asyncio.wait([e.edit("`" + e.text + "`")])
          
@register(incoming=True)
async def autoReply(e):
  if e.is_private and not (await e.get_sender()).bot:
    global mutedList
    if e.chat_id in mutedList:
      await e.delete()
    else:
      if type((await e.client.get_me()).status).__name__ ==  "UserStatusOffline":
        global exempt
        if not e.sender.id in exempt:
          exempt.append(e.sender.id)
          x = 0
          while True:
            if type((await e.client.get_me()).status).__name__ ==  "UserStatusOffline":
              await asyncio.sleep(1)
              x += 1
              if x >= 300:
                global message
                await e.respond(message)
                exempt.remove(e.sender.id)
                break
            else:
              exempt.remove(e.sender.id)
              break
@register(outgoing=True, pattern="^.speedtest")
async def speedtest(event):
    if event.fwd_from:
        return
    input_str = str(message[6:8])
    as_text = False
    as_document = True
    if input_str == "image":
        as_document = False
    elif input_str == "file":
        as_document = True
    elif input_str == "text":
        as_text = True
    await event.edit("Calculating my internet speed. Please wait!")
    start = datetime.now()
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    response = s.results.dict()
    download_speed = response.get("download")
    upload_speed = response.get("upload")
    ping_time = response.get("ping")
    client_infos = response.get("client")
    i_s_p = client_infos.get("isp")
    i_s_p_rating = client_infos.get("isprating")
    reply_msg_id = event.message.id
    if event.reply_to_msg_id:
        reply_msg_id = event.reply_to_msg_id
    try:
        response = s.results.share()
        speedtest_image = response
        if as_text:
            await event.edit("""**SpeedTest** completed in {} seconds
Download: {}
Upload: {}
Ping: {}
Internet Service Provider: {}
ISP Rating: {}""".format(ms, convert_from_bytes(download_speed), convert_from_bytes(upload_speed), ping_time, i_s_p, i_s_p_rating))
        else:
            await borg.send_file(
                event.chat_id,
                speedtest_image,
                caption="**SpeedTest** completed in {} seconds".format(ms),
                force_document=as_document,
                reply_to=reply_msg_id,
                allow_cache=False
            )
            await event.delete()
    except Exception as exc:
        await event.edit("""**SpeedTest** completed in {} seconds
Download: {}
Upload: {}
Ping: {}
__With the Following ERRORs__
{}""".format(ms, convert_from_bytes(download_speed), convert_from_bytes(upload_speed), ping_time, str(exc)))


def convert_from_bytes(size):
    power = 2**10
    n = 0
    units = {
        0: "",
        1: "kilobytes",
        2: "megabytes",
        3: "gigabytes",
        4: "terabytes"
    }
    while size > power:
        size /= power
        n += 1
    return f"{round(size, 2)} {units[n]}"
