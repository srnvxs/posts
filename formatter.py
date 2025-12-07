def build_text(anime):
    title = anime.get("title", "Unknown Anime")
    synopsis = anime.get("description", "Synopsis not available.")

    # Clean AniList HTML breaks
    synopsis = synopsis.replace("<br>", "\n") \
                       .replace("<br/>", "\n") \
                       .replace("<br />", "\n")

    # Remove empty lines & take first 7 lines only
    lines = [line.strip() for line in synopsis.split("\n") if line.strip()]
    synopsis_7 = "\n".join(lines[:7])

    text = f"""
<b>{title}</b>
────────────────────────
<b>➤ Season :</b> <code>1</code>
<b>➢ Audio :</b> <code>Jap • Eng • Hin • Tel • Tam</code>
<b>➤ Quality :</b> <code>480ᴘ • 720ᴘ • 1080ᴘ</code>
<b>➥ Episodes :</b> —
<blockquote expandable><b>➟ sʏɴᴏᴘsɪs :</b> <i>{synopsis_7}</i></blockquote>
────────────────────────
💠 <b>Powered By</b> : @OtakusFlix
""".strip()

    # Force RAW text (no Telegram formatting)
    return text.replace("<", "&lt;").replace(">", "&gt;")
