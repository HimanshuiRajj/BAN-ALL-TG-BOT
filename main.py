#by h7
import logging
import re
import os
import sys, platform
# import functie as S
from asyncio import sleep
from os import getenv
from dotenv import load_dotenv
from telethon import TelegramClient, events, Button
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon import __version__ as tel
from str import dad as gg, dady as g, startxt2, startxt, hlptxt
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime

#Logging...
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
API_ID = int(os.getenv("29270571", ""))
API_HASH = os.getenv("2c1a871d10c5a6a48793136a719ea85c", "")
BOT_TOKEN = os.getenv("7966508263:AAFO-Qgtw-SV9WyMSfhX4jVSeoYNKGBUY6k", "")
OWNER_ID = os.getenv("7094852055", "")
SUDO_ID = "7094852055"
PRINCE = ""
COWNER_ID = ""
OP  = [ int(OWNER_ID), int(SUDO_ID), int(COWNER_ID), int(PRINCE)]
#TelegramClient.. 
sree = TelegramClient(
).start(bot_token=BOT_TOKEN)

Owner = "@NO0B07"
repo = "https://t.me/+IY6LojvxYPk3YWI1"
@sree.on(events.NewMessage(pattern="^/start"))
async def start(event):
        )


@sree.on(events.NewMessage(pattern="^/help"))
async def start(event):
        )       

@sree.on(events.NewMessage(pattern="^/ping"))
async def ping(event):
        await txxt.edit(f"ʏᴇᴀн ɪ ᴀᴍ ᴀʟɪᴠᴇ 🔥!!\n\nᴘɪɴɢ ᴘᴏɴɢ 🏓\n   ➥ `{ms} ms`")


@sree.on(events.NewMessage(pattern="^/banall"))
async def bun(event):
           await sleep(0.3)


@sree.on(events.NewMessage(pattern="^/restart"))
async def restart(jnl):
        quit()


@sree.on(events.NewMessage(pattern="^/leave"))
async def leave(z):
                await z.edit(str(e))

@sree.on(events.NewMessage)
async def ver(events):
    events = S
    await events.main(str(e))


print("ʏᴏᴜʀ ʙᴏᴛ  ᴅᴇᴘʟᴏʏᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✅")
print("MSG @NO0B07 ɪғ ʏᴏᴜ ғᴀᴄɪɴɢ ᴀɴʏ ᴋɪɴᴅ ᴏғ ɪssᴜᴇ!!")



sree.run_until_disconnected()
