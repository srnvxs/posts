import re

FONT_MAP = {
    "a":"ᴀ","b":"ʙ","c":"ᴄ","d":"ᴅ","e":"ᴇ","f":"ꜰ","g":"ɢ","h":"ʜ",
    "i":"ɪ","j":"ᴊ","k":"ᴋ","l":"ʟ","m":"ᴍ","n":"ɴ","o":"ᴏ","p":"ᴘ",
    "q":"ǫ","r":"ʀ","s":"s","t":"ᴛ","u":"ᴜ","v":"ᴠ","w":"ᴡ","x":"x",
    "y":"ʏ","z":"ᴢ"
}

def fancy(text: str):
    return "".join(FONT_MAP.get(c.lower(), c) for c in text)

def build_text(anime):
    title = anime.get("title", "Unknown Anime").upper()
    synopsis = anime.get("description", "Synopsis not available.")

    # Remove HTML tags
    synopsis = re.sub(r"<.*?>", "", synopsis)

    # Take first 7 sentences
    sentences = re.split(r'(?<=[.!?]) +', synopsis.strip())
    synopsis_7 = " ".join(sentences[:7])

    synopsis_fancy = fancy(synopsis_7)

    text = f"""
<b>{title}</b>
────────────────────────
<b>➤ Season :</b> <code>1</code>
<b>➢ Audio :</b> <code>Jap • Eng • Hin • Tel • Tam</code>
<b>➤ Quality :</b> <code>480ᴘ • 720ᴘ • 1080ᴘ</code>
<b>➥ Episodes :</b> —
<blockquote expandable><b>➟ sʏɴᴏᴘsɪs :</b> <i>{synopsis_fancy}</i></blockquote>
────────────────────────
💠 <b>Powered By</b> : @OtakusFlix
""".strip()

    # Raw HTML text only
    return text.replace("<", "&lt;").replace(">", "&gt;")
