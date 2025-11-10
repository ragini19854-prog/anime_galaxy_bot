import telebot
from telebot import types

# ────────────────────────────────
# ⚠️ Replace this with YOUR real bot token (keep it private!)
BOT_TOKEN = "8582546752:AAERruMSS_szYBuI4VrZL2mXMAAATkdJAQ0"
CHANNEL_ID = -1003087486594
CHANNEL_LINK = "https://t.me/chill_and_chat_2_3"
# ────────────────────────────────

bot = telebot.TeleBot(BOT_TOKEN)

# 🔹 Anime Database (directly in Python)
anime_data = {
    "Doremon": "https://t.me/Doremon_In_Hindi_Dubed",
    "Pokemon": "https://t.me/Pokemon_In_Dub_Hindi",
    "Parman": "https://t.me/parmanepisods",
    "I am getting married to a girl I hate in my class": "https://t.me/iamhebes",
    "naruto": "https://t.me/Naruto_Shippuden_in_HindiDubb",
    "jujutsu kaisen": "https://t.me/+PoJtNvoMs4NlY2I9",
    "dragon ball": "https://t.me/Dragon_Ball_in_English_Dub",
    "tokyo revengers season 2": "https://t.me/+lv52oEjIDqYwNzBl",
    "one punch man": "https://t.me/+ERdHxJC9obdjZTU1",
    "baki": "https://t.me/baki_hindi",
    "black clover": "https://t.me/+-RNZmRHnaWswYWU1",
    "darling in the franxx": "https://t.me/hindi_darling_in_the_franxx",
    "akebi's sailor uniform": "https://t.me/Akebis_Sailor_Uniform_Hindi",
    "death note": "https://t.me/death_note_ind",
    "magi: the labyrinth of magic": "https://t.me/magi_the_labyrinth_magic_hindi",
    "scum’s wish": "https://t.me/scums_wish_in_hindi",
    "tomodachi game": "https://t.me/tomodachi_game_in_hindi",
    "hitman reborn": "https://t.me/hindi_hitman_reborn",
    "hentai": "https://t.me/+M6P499fOf8c5N2U1",
    "the reincarnation of the strongest exorcist in another world": "https://t.me/reincarnation_strongest_in_hindi",
    "twin star exorcists": "https://t.me/Twin_star_exorcist_hindi",
    "demon slayer": "https://t.me/+UPlJliNxAyI3NTE1",
    "the apothecary diaries": "https://t.me/+E7ZuKXIu7gs3MGQ1",
    "i was reincarnated as the 7th prince": "https://t.me/+nyLRtoqyer4wYzk1",
    "solo leveling": "https://t.me/Solo_Leveling_Season_1_2_Hindi",
    "my happy marriage": "https://t.me/My_Happy_Marriage_In_Hindi_Dubbe",
    "blue lock": "https://t.me/Blue_Lock_In_Official_Hindi_Dub",
    "bye bye earth": "https://t.me/bye_bye_earth_season2_in_hindi",
    "the iceblade sorcerer shall rule the world": "https://t.me/Download_In_Hindi_12",
    "the strongest magician in the demon lord": "https://t.me/The_Strongest_Magician_in_Hindi1",
    "the daily life of the immortal king": "https://t.me/The_Daily_life_immortal_King_35",
    "re:zero": "https://t.me/Rezero_Dub_Hindi",
    "hunter × hunter season 5": "https://t.me/Hunter_x_Hunter_Hindi_Dubbbb",
    "my love story with yamada-kun at lv999": "https://t.me/+40IBmhtzDlE4NWY1",
    "viral hit": "https://t.me/+Kwum2a1m0sMxYzc9",
    "a condition called love": "https://t.me/+9dz-1WccpsFhYThl",
    "devil may cry": "https://t.me/+znc2LNAm1BQ3MzVl",
    "i parry everything": "https://t.me/+SbuBeu0ZLVE1OTll",
    "with you, our love will make it through": "https://t.me/+l9YsNGwAYM82MGVl",
    "dr stone": "https://t.me/+nTJG9u3Igq5jMzBl",
    "tsukimichi moonlit fantasy": "https://t.me/+41wV-1aWF_Y2NGNl",
    "fragment flower boom with dignity": "https://t.me/+a6hrOZnE9yMyYTNl",
    "rurouni kenshin": "https://t.me/+IltCoZtCuGllOGU1",
    "i got a cheat skill in another world": "https://telegra.ph/I-Got-a-Cheat-Skill-in-Another-World-04-03",
    "kamikatsu: working for a god in a godless world": "https://t.me/+f5paTnk9E-phNmRl",
    "overflow": "https://t.me/+cXNtKxjFwndmYTZl",
    "attack on titan": "https://t.me/+lum5df8V33Y4NGFl",
    "spider-man": "https://t.me/+rEHwDH1unZZmYmQ9",
    "one piece": "https://t.me/+aR_KqNGZJNVhNjc1",
    "summer time rendering": "https://t.me/+-lMdxOVL0_IxMzk1",
    "grave of the fireflies": "https://t.me/+PlT3sMMbwjpjNDZl",
    "horimiya": "https://t.me/+Ska51U9Nt49lODQ9",
    "rascal does not dream": "https://t.me/+xxnjwI-JOmMyM2I1",
    "the angel next door spoils me rotten": "https://t.me/+G5QC6m0KD3U0ZDBl",
    "black butler": "https://t.me/+ILHEHm84HG03MjE1",
    "shangri-la frontier": "https://t.me/+5MR4j5RXH4diMjg1"
}

# 🔹 Helper: check if user joined channel
def is_user_joined(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False

# 🔹 /start command
@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    if is_user_joined(user_id):
        bot.send_message(message.chat.id, "✅ Welcome to Anime Galaxy by Madara!\n\nType any anime name to get its link 🔍")
    else:
        markup = types.InlineKeyboardMarkup()
        join_btn = types.InlineKeyboardButton("Click to Join Channel", url=CHANNEL_LINK)
        markup.add(join_btn)
        bot.send_message(message.chat.id, "⚠️ To use this bot, join our official channel first!", reply_markup=markup)
        bot.send_message(message.chat.id, "After joining, send **yes** to continue.", parse_mode="Markdown")

# 🔹 After joining
@bot.message_handler(func=lambda m: m.text and m.text.lower() == "yes")
def verify_join(message):
    user_id = message.from_user.id
    if is_user_joined(user_id):
        bot.send_message(message.chat.id, "🌌 Welcome to Anime Galaxy by Madara!")
        bot.send_message(message.chat.id, "📘 *How to use the bot:*\n1️⃣ Type any anime name\n2️⃣ The bot will reply with the link\n3️⃣ Works in both groups & DMs", parse_mode="Markdown")
        bot.send_message(message.chat.id, "⚠️ All The Content in this Channel is Either Taken From the Internet.\nWe Don't Own Any Content.\nWe just index those links already available online.")
    else:
        bot.send_message(message.chat.id, "❌ You haven’t joined our channel yet.")

# 🔹 Anime link handler
@bot.message_handler(func=lambda message: True)
def reply_with_link(message):
    name = message.text.lower().strip()
    if name in anime_data:
        bot.reply_to(message, anime_data[name])
    else:
        if message.chat.type == "private":
            bot.reply_to(message, "We will provide it soon 😊")

bot.infinity_polling()
