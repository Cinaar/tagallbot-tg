# Changing some lines of code won't make you a programmer.
# Use with credits else gay.
# © by Akhil (@AKH1LS).


import os, logging, asyncio
from telethon import InlineKeyboardMarkup, InlineKeyboardButton
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
spam_chats = []

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply(
    "**Hello, I am Tag All Bot**, I can help your groups to mention users with mass quantity with a single command.\nDo ``/help`` to know more.",
    link_preview=False,
    reply_markup = InlineKeyboardMarkup(

        [

            [

                InlineKeyboardButton(

                    text="Open Link",

                    url=f"https://pixeldrain.com/u/{data['id']}"

                ),

                InlineKeyboardButton(

                ,    text="Share Link",

                    url=f"https://telegram.me/share/url?url=https://pixeldrain.com/u/{data['id']}"

                )

            ],

            [

                InlineKeyboardButton(text="Join Updates Channel", url="https://telegram.me/FayasNoushad")

            ]

        ]

    )

@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**Help Menu of TagAllBot**\n\nCommand: /all\nYou can use this command with text what you want to mention others.\nExample: `/all Hii!`\nYou can you this command as a reply to any message. Bot will tag users to that replied messsage.\n\nUse /cancel to stop tagging in group\n\nFollow [Akhil](https://telegram.me/AKH1LS) on Telegram to be updated..!!"
  await event.reply(
    helptext,
    link_preview=False,
    buttons=(
      [
        Button.url('Support', 'https://telegram.me/BlueCodeSupport'),
        Button.url('Creator', 'https://telegram.me/AKH1LS')
      ]
    )
  )
 
@client.on(events.NewMessage(pattern="^/repo$"))
async def start(event):
  await event.reply(
    "**I am *AKIRA* superfast Tagger bot made for your groups. A fully open sourced bot for you. Click below to know my Source...",
    link_preview=False,
    buttons=(
      [
        Button.url('Source Code', 'https://github.com/SpectraXCode/tagallbot-tg'),
        Button.url('Chat with us', 'https://telegram.me/HELL_X_CHATS')
      ]
    )
  )
 
@client.on(events.NewMessage(pattern="^/all ?(.*)"))
async def all(event):
  chat_id = event.chat_id
  if event.is_private:
    return await event.respond("This command can only be used in groups to tag members...")
  
  is_admin = False
  try:
    partici_ = await client(GetParticipantRequest(
      event.chat_id,
      event.sender_id
    ))
  except UserNotParticipantError:
    is_admin = False
  else:
    if (
      isinstance(
        partici_.participant,
        (
          ChannelParticipantAdmin,
          ChannelParticipantCreator
        )
      )
    ):
      is_admin = True
  if not is_admin:
    return await event.respond("Only Admins can use me\n\nFor any query join @BlueCodeSupport !")
  
  if event.pattern_match.group(1) and event.is_reply:
    return await event.respond("__Give me one argument!__")
  elif event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.is_reply:
    mode = "text_on_reply"
    msg = await event.get_reply_message()
    if msg == None:
        return await event.respond("I can't mention members for older messages! (messages which are sent before I'm added to group) ")
  else:
    return await event.respond("Reply to a message or give Me some text To mention members\n\nMade bY @AKH1LS !")
  
  spam_chats.append(chat_id)
  usrnum = 0
  usrtxt = ''
  async for usr in client.iter_participants(chat_id):
    if not chat_id in spam_chats:
      break
    usrnum += 1
    usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
    if usrnum == 5:
      if mode == "text_on_cmd":
        txt = f"{usrtxt}\n\n{msg}\n\nMade by @AKH1LS. Subscribe the channel to be updated..!!"
        await client.send_message(chat_id, txt)
      elif mode == "text_on_reply":
        await msg.reply(usrtxt)
      await asyncio.sleep(2)
      usrnum = 0
      usrtxt = ''
  try:
    spam_chats.remove(chat_id)
  except:
    pass

@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
  if not event.chat_id in spam_chats:
    return await event.respond('There Is No Proccess... what should I cancel ?')
  else:
    try:
      spam_chats.remove(event.chat_id)
    except:
      pass
    return await event.respond('**Stopped Mention !**')

print("Bot started successfully... Made by @AKH1LS. Subscribe the channel to be updated..!!")
client.run_until_disconnected()
