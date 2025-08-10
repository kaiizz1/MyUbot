from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


flood = {}
OLD_MSG = {}
MSG_PERMIT = (
    """
╔═════════════════════╗
│  𖣘 𝚂𝙴𝙻𝙰𝙼𝙰𝚃 𝙳𝙰𝚃𝙰𝙽𝙶 𝚃𝙾𝙳 𖣘ㅤ  ㅤ
╚═════════════════════╝
 ⍟ 𝙹𝙰𝙽𝙶𝙰𝙽 𝚂𝙿𝙰𝙼 𝙲𝙷𝙰𝚃 𝙼𝙰𝙹𝙸𝙺𝙰𝙽 𝙶𝚄𝙰 𝙺𝙴𝙽𝚃𝙾𝙳
 ⍟ 𝙶𝚄𝙰 𝙰𝙺𝙰𝙽 𝙾𝚃𝙾𝙼𝙰𝚃𝙸𝚂 𝙱𝙻𝙾𝙺𝙸𝚁 𝙺𝙰𝙻𝙾 𝙻𝚄 𝚂𝙿𝙰𝙼
 ⍟ 𝙹𝙰𝙳𝙸 𝚃𝚄𝙽𝙶𝙶𝚄 𝚂𝙰𝙼𝙿𝙰𝙸 𝙼𝙰𝙹𝙸𝙺𝙰𝙽 𝙶𝚄𝙰 𝙽𝙴𝚁𝙸𝙼𝙰 𝙿𝙴𝚂𝙰𝙽 𝙻𝚄
╔═════════════════════╗
│ㅤㅤ𖣘 𝙿𝙴𝚂𝙰𝙽 𝙾𝚃𝙾𝙼𝙰𝚃𝙸𝚂 𖣘ㅤㅤ
│ㅤㅤ   𖣘 ᴋᴀɪɪ - 𝚄𝙱𝙾𝚃 𖣘ㅤㅤ
╚═════════════════════╝
"""
)


class Var:
    API_HASH = getenv("API_HASH")
    API_ID = int(getenv("API_ID", "22398048"))
    ALIVE_PIC = getenv("ALIVE_PIC", "https://files.catbox.moe/6iag43.jpg")
    ALIVE_TEXT = getenv("ALIVE_TEXT", "Hey, Saya KaiiUbot Dibuat dengan basis pyrogram versi terbaru")
    BOT_TOKEN = getenv("BOT_TOKEN", "8392634276:AAEwFnojQodWKF9TLxzmbUkORFZE-Ikszoc")
    BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
    if not BLACKLIST_CHAT:
        BLACKLIST_CHAT = [-1001473548283, -1001675396283]
    LOG_CHAT = int(getenv("LOG_CHAT") or 0)
    HNDLR = getenv("HNDLR", [".", "!", "*", "^", "-", "?"])
    DB_URL = getenv("DATABASE_URL", "")
    HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
    MONGO_URI = getenv("MONGO_URI", None)
    NO_LOAD = [int(x) for x in getenv("NO_LOAD", "").split()]
    PMPERMIT = bool(getenv("PMPERMIT", True))
    PERMIT_MSG = str(getenv("PERMIT_MSG", MSG_PERMIT))
    PERMIT_LIMIT = int(getenv("PERMIT_LIMIT", 5))
    REM_BG_API_KEY = getenv("REM_BG_API_KEY", "6rk2bSt7Q2mrdFw9Dv4hTLLS")
    STRING_1 = getenv("STRING_1", "1BVtsOLoBu4HiEnq5ctPYUKOcjjzzlnwBwDgRFAUdgpAyYKOCFs0h51wX56XPq7zKWdD6xg0pmLPudbsG6xmpLS3ogAMHIHGUSaTZ_mhmWm0gdWdjxtsdT2DnmzTZ19UaOaxdIQdYPosK1OoQLm32XBEHkATORgDZ9punQjDqAJxS3awKDr79ZzJICfbAt0-g6qUfzn_DP2Szq8bNdlZzLOC2Sg2wwSLW8gLjF1ZO2KOiuzx-KfF-rMNObyIuUM5aiB2-ZX-dns-WUv9V6hV9ErAouajwoLQAoIorr6ZFyjiX5uYs4XcWbVHoOwnTe7e7Qd7B1zPiEGdWOETPepYnYt-rq2Hq2fM=")
    STRING_2 = getenv("STRING_2", "BQFVxGAABXDxDFB9SY2pxo_wxW38P0QM3UkUIYNXgGJr2KkJ2PiQuJfkV5HzGedu2SIJfd_1UjMkK9sg4Jlojg4XlA2wkdYGqJvIzvh84FjJRh_mltkcyV6w1VegJL1PuksGijX0yiGACqbyfLwK2JnjYdTcQThUrGdJQ8KoBfXXvAzgP_IDyzn3vreDnb5WPk0JOOKX34GFWM5exjTUJKjjlGsJ6-8Y2wPN6yrFsI7VUFLOEu0izihUbVWCKPHWam8YFm2TxZqn-l9-SnQInsogHymcohHPNeoVP-XJr9Bajzm2ffIyjESJuscdN234o9nuNjxR70B2pjnW8yxxU7zEYuI8RQAAAAGPV69iAA")
    STRING_3 = getenv("STRING_3", "")
    STRING_4 = getenv("STRING_4", "")
    STRING_5 = getenv("STRING_5", "")
    TEMP_DOWNLOAD_DIRECTORY = getenv("TMP_DOWNLOAD_DIRECTORY", "./downloads/")
    TZ = getenv("TZ", "Asia/Jakarta")
