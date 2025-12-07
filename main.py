from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN
from anilist import get_anime
from formatter import build_text

bot = Client(
    "AnimeTextBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.private & filters.text)
async def anime_handler(client, message):
    anime = get_anime(message.text)

    if not anime:
        await message.reply_text("Anime not found.")
        return

    output = build_text(anime)

    # parse_mode is intentionally NOT used
    await message.reply_text(
        output,
        disable_web_page_preview=True
    )

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "Send anime name.\nOutput will be RAW HTML TEXT."
    )

bot.run()
