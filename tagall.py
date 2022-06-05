# Changing some lines of code won't make you a programmer.
# use with credits else gay.
# © By @AKH1LS.

import os, logging, asyncio

from telegraph import upload_file

from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
AJ = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

moment_worker = []


# here replace "AkiraTaggerBot" with your own bot username.
# use with credits else gay.

@AJ.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("Hello, I am TagAll Bot.\nI can help you to tag group members with less time in mass quantity.\nIf you have any query, do /help ",
                    buttons=(
                      [
                         Button.url('Support', 'https://telegram.dog/Akira_Support'), 
                         Button.url('Creator', 'https://telegram.dog/AKH1LS'), 
                      ], 
                      [
                        Button.url('➕ ADD ME TO YOUR GROUP ➕', 'https://t.me/AkiraTaggerBot?startgroup=true'),   
                      ]
                   ), 
                    link_preview=False
                   )

# here also replace "AkiraTaggerBot" with your own bot username.
# use with credits else gay.

@AJ.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**Tag Help Bot's Help Menu**\n\nCommand: /all \n You can use this command with text you want to tell others. \n`Example: /all Hii!` \nYou can use this command as an answer. any message Bot will tag users to replied message."
  await event.reply(helptext,
                    buttons=(
                      [
                         Button.url('Support', 'https://telegram.dog/Akira_Support'), 
                         Button.url('Creator', 'https://telegram.dog/AKH1LS'), 
                      ], 
                      [
                        Button.url('➕ ADD ME TO YOUR GROUP ➕', 'https://t.me/AkiraTaggerBot?startgroup=true'),   
                      ]
                   ), 
                    link_preview=False
                   )

@AJ.on(events.NewMessage(pattern="^/repo$"))
async def repo(event):
  repotext = "I am an open source bot made by [Akhil](https://telegram.dog/AKH1LS)."
  await event.reply(repotext,
                    buttons=(
                      [
                         Button.url('Source Code', 'https://github.com/SpectraXCode/tagallbot-tg'), 
                         Button.url('Creator', 'https://telegram.dog/AKH1LS'), 
                      ], 
                      [
                        Button.url('➕ ADD ME TO YOUR GROUP ➕', 'https://t.me/AkiraTaggerBot?startgroup=true'),   
                      ]
                   ), 
                    link_preview=False
                   )

@AJ.on(events.NewMessage(pattern="^/tagall|/call|/tall|/all|#all|@all?(.*)"))
async def mentionall(event):
  global moment_worker
  if event.is_private:
    return await event.respond("Use this command in channel or group!")
  
  admins = []
  async for admin in AJ.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("Only admin can use it.")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("I can't Mention Members for Old Post!")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Give me an Argument. Ex: `/tag Hii, Where are you`")
  else:
    return await event.respond("Reply to Message or Give Some Text To Mention!")
    
  if mode == "text_on_cmd":
    moment_worker.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in AJ.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await event.respond("Stopped!")
        return
      if usrnum == 5:
        await AJ.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    moment_worker.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in AJ.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await event.respond("Stopped")
        return
      if usrnum == 5:
        await AJ.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@AJ.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
  if not event.chat_id in spam_chats:
    return await event.respond('Nothing to cancel...)
  else:
    try:
      spam_chats.remove(event.chat_id)
    except:
      pass
    return await event.respond('**Stopped mention...**')


print("Connecting...")
print("Started Successfully....")
print("Made by @AKH1LS. Join the channel to be updated !")
AJ.run_until_disconnected()


# MADE UNDER AKIRA PROJECT
