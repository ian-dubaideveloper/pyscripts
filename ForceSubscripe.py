
import asyncio
import requests


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant


bot = Client(
    "Bot",
    api_id = 1,
 api_hash = "a",
 bot_token = "bibQYCTDpJcHslPDzXJ7J1Jg"
)

bot_token = "7bibQYCTDpJcHslPDzXJ7J1Jg"   # Your Bot Token
CHANNEL = "Y88F8"   #Your channel username without @ 

       
@bot.on_message(filters.command("start") & filters.private)
async def start(client: Client, message: Message):
       m = message.chat.id
       user = message.from_user.mention
       do = requests.get(f"https://api.telegram.org/bot{bot_token}/getChatMember?chat_id=@{CHANNEL}&user_id={message.from_user.id}").text
       if do.count("left") or do.count("Bad Request: user not found"):
          await message.reply_text(f"**Join [this channel](t.me/{CHANNEL}) first to be able to use the bot ✨**", disable_web_page_preview=True,
          reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                        "Join Channel ✨ .",
                        url=f'https://t.me/{CHANNEL}'),
                        ],
                    ]
                )
            ) 
       else:
         await bot.send_message(m, f"**Hello my friend ( {user} ) **",
       reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                        "🇸🇾 Dev .",
                        url=f'https://t.me/ZDDDU'),
                        ],[
                            InlineKeyboardButton(
                        "- More bots ✨",
                        url=f'https://t.me/Y88F8'),
                        ],
                    ]
                )
            ) 
            
            
            
            
print("""
███████╗░█████╗░██╗██████╗░
╚════██║██╔══██╗██║██╔══██╗
░░███╔═╝███████║██║██║░░██║
██╔══╝░░██╔══██║██║██║░░██║
███████╗██║░░██║██║██████╔╝
╚══════╝╚═╝░░╚═╝╚═╝╚═════╝░

codded by : Ian DubaiDeveloper""")
bot.run()            