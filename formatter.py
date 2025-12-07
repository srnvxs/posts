def build_text(anime):
    title = anime.get("title", "Unknown Anime")
    synopsis = anime.get("description", "Synopsis not available.")

    text = f"""
<b>{title}</b>
────────────────────────
<b>➤ Season :</b> <code>1</code>
<b>➢ Audio :</b> <code>Jap • Eng • Hin • Tel • Tam</code>
<b>➤ Quality :</b><code> 480ᴘ • 720ᴘ • 1080ᴘ</code>
<b>➥ Episodes :</b> —
<blockquote expandable><b>➟ sʏɴᴏᴘsɪs :</b> <i>{synopsis}</i></blockquote>
────────────────────────
💠 <b>Powered By</b> : @OtakusFlix
"""
    return text.strip()
