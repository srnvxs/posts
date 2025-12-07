import re

def build_text(anime):
    title = anime.get("title", "Unknown Anime")
    synopsis = anime.get("description", "Synopsis not available.")

    # Remove HTML tags from AniList text
    synopsis = re.sub(r"<.*?>", "", synopsis)

    # Stop before special episodes section
    stop_phrases = [
        "This includes",
        "Special Episode",
        "Following special",
        "Includes following"
    ]

    for phrase in stop_phrases:
        if phrase in synopsis:
            synopsis = synopsis.split(phrase)[0]

    # Split into sentences and take first 7
    sentences = re.split(r'(?<=[.!?]) +', synopsis.strip())
    synopsis_7 = " ".join(sentences[:7])

    text = f"""
<b>{title.upper()}</b>
────────────────────────
<b>➤ Season :</b> <code>1</code>
<b>➢ Audio :</b> <code>Jap • Eng • Hin • Tel • Tam</code>
<b>➤ Quality :</b> <code>480ᴘ • 720ᴘ • 1080ᴘ</code>
<b>➥ Episodes :</b> —
<blockquote expandable><b>➟ sʏɴᴏᴘsɪs :</b> <i>{synopsis_7}</i></blockquote>
────────────────────────
💠 <b>Powered By</b> : @OtakusFlix
""".strip()

    # Show HTML tags as RAW TEXT
    return text.replace("<", "&lt;").replace(">", "&gt;")
