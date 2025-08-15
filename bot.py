
import os
import telebot

# ================== CONFIG ==================
TOKEN = os.environ.get("BOT_TOKEN")  # Set on Render (Environment Variables)
DEFAULT_LANG = os.environ.get("DEFAULT_LANG", "ru")
# ============================================

if not TOKEN:
    raise RuntimeError("BOT_TOKEN is not set. Define it as an environment variable.")

bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")

TEXTS = {
    "ru": {
        "start": "👋 Привет! Я *PabloFoxFinderBot* — твой шорткат к лучшим офферам.\nВыбирай, что делать дальше:",
        "menu": "Главное меню:",
        "find": "Напиши, что ищем (например: *iphone 15 case*):",
        "categories": "Выбери категорию:",
        "tracking_saved": "Принял! Я запомнил, позже пришлю, когда цена снизится (демо).",
        "help": "Команды:\n/start — меню\n/find — поиск\n/categories — категории\n/track — трек цены\n/help — помощь\n/lang — язык",
        "lang": "Выбери язык:",
        "lang_set": "Язык переключен на: Русский 🇷🇺",
        "please_query": "Отправь поисковый запрос текстом.",
        "unknown": "Пока не понимаю. Нажми кнопку меню 🙂",
        "btn_search": "🔎 Поиск",
        "btn_categories": "📂 Категории",
        "btn_track": "📉 Трек цены",
        "btn_lang": "🌐 Язык / Language",
        "btn_help": "❓ Помощь",
        "back": "⬅️ Назад",
    },
    "en": {
        "start": "👋 Hey! I’m *PabloFoxFinderBot* — your shortcut to top deals.\nChoose what to do next:",
        "menu": "Main menu:",
        "find": "Type what to search (e.g., *iphone 15 case*):",
        "categories": "Pick a category:",
        "tracking_saved": "Got it! I’ll track it and ping you if the price drops (demo).",
        "help": "Commands:\n/start — menu\n/find — search\n/categories — categories\n/track — price track\n/help — help\n/lang — language",
        "lang": "Choose language:",
        "lang_set": "Language set to: English 🇬🇧",
        "please_query": "Send a text query.",
        "unknown": "I don’t get it yet. Use the menu 🙂",
        "btn_search": "🔎 Search",
        "btn_categories": "📂 Categories",
        "btn_track": "📉 Price track",
        "btn_lang": "🌐 Language",
        "btn_help": "❓ Help",
        "back": "⬅️ Back",
    },
}

CATEGORIES = [
    ("Electronics ⚡️", "electronics"),
    ("Phones & Accessories 📱", "smartphone"),
    ("Computer & Office 💻", "laptop"),
    ("Home & Garden 🏡", "home decor"),
    ("Beauty & Health 💄", "cosmetics"),
]

from urllib.parse import quote_plus
from telebot import types

user_langs = {}
awaiting_query = set()
awaiting_track = set()

def get_lang(chat_id): return user_langs.get(chat_id, DEFAULT_LANG)
def set_lang(chat_id, lang): user_langs[chat_id] = lang
def t(chat_id, key): return TEXTS[get_lang(chat_id)][key]

def main_menu_kb(chat_id):
    lang = get_lang(chat_id)
    m = types.InlineKeyboardMarkup()
    m.row(
        types.InlineKeyboardButton(TEXTS[lang]["btn_search"], callback_data="menu_find"),
        types.InlineKeyboardButton(TEXTS[lang]["btn_categories"], callback_data="menu_categories")
    )
    m.row(types.InlineKeyboardButton(TEXTS[lang]["btn_track"], callback_data="menu_track"))
    m.row(
        types.InlineKeyboardButton(TEXTS[lang]["btn_lang"], callback_data="menu_lang"),
        types.InlineKeyboardButton(TEXTS[lang]["btn_help"], callback_data="menu_help"),
    )
    return m

def categories_kb(chat_id):
    lang = get_lang(chat_id)
    m = types.InlineKeyboardMarkup()
    for name, code in CATEGORIES:
        m.row(types.InlineKeyboardButton(name, callback_data=f"cat::{code}"))
    m.row(types.InlineKeyboardButton(TEXTS[lang]["back"], callback_data="menu_back"))
    return m

def lang_kb(chat_id):
    m = types.InlineKeyboardMarkup()
    m.row(types.InlineKeyboardButton("Русский 🇷🇺", callback_data="lang::ru"))
    m.row(types.InlineKeyboardButton("English 🇬🇧", callback_data="lang::en"))
    m.row(types.InlineKeyboardButton(TEXTS[get_lang(chat_id)]["back"], callback_data="menu_back"))
    return m

def build_affiliate_link(query: str) -> str:
    base = "https://aliexpress.com/wholesale?SearchText="
    # TODO: вставь реальные партнёрские параметры ниже (AliExpress PID/SUBID)
    tracking = "&aff_fcid=DEMO&aff_fsk=DEMO&aff_platform=portals-tool&sk=DEMO"
    return base + quote_plus(query) + tracking

bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")

@bot.message_handler(commands=['start'])
def cmd_start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, t(chat_id, "start"), reply_markup=main_menu_kb(chat_id))

@bot.message_handler(commands=['help'])
def cmd_help(message):
    bot.send_message(message.chat.id, t(message.chat.id, "help"), reply_markup=main_menu_kb(message.chat.id))

@bot.message_handler(commands=['find'])
def cmd_find(message):
    chat_id = message.chat.id
    awaiting_query.add(chat_id)
    bot.send_message(chat_id, t(chat_id, "find"))

@bot.message_handler(commands=['categories'])
def cmd_categories(message):
    bot.send_message(message.chat.id, t(message.chat.id, "categories"), reply_markup=categories_kb(message.chat.id))

@bot.message_handler(commands=['track'])
def cmd_track(message):
    chat_id = message.chat.id
    awaiting_track.add(chat_id)
    bot.send_message(chat_id, "Отправь ссылку или запрос, который трекать:" if get_lang(chat_id)=="ru"
                     else "Send a link or query to track:")

@bot.message_handler(commands=['lang'])
def cmd_lang(message):
    bot.send_message(message.chat.id, t(message.chat.id, "lang"), reply_markup=lang_kb(message.chat.id))

@bot.callback_query_handler(func=lambda c: True)
def on_callback(call):
    data = call.data or ""
    chat_id = call.message.chat.id

    if data == "menu_find":
        awaiting_query.add(chat_id)
        bot.send_message(chat_id, t(chat_id, "find"))
    elif data == "menu_categories":
        bot.send_message(chat_id, t(chat_id, "categories"), reply_markup=categories_kb(chat_id))
    elif data == "menu_track":
        awaiting_track.add(chat_id)
        bot.send_message(chat_id, "Отправь ссылку или запрос, который трекать:" if get_lang(chat_id)=="ru"
                         else "Send a link or query to track:")
    elif data == "menu_help":
        bot.send_message(chat_id, t(chat_id, "help"))
    elif data == "menu_lang":
        bot.send_message(chat_id, t(chat_id, "lang"), reply_markup=lang_kb(chat_id))
    elif data == "menu_back":
        bot.send_message(chat_id, t(chat_id, "menu"), reply_markup=main_menu_kb(chat_id))
    elif data.startswith("cat::"):
        q = data.split("::",1)[1]
        link = build_affiliate_link(q)
        bot.send_message(chat_id, f"🔗 {link}\n\n(демо-ссылка; позже подставим твой партнёрский ID)")
    elif data.startswith("lang::"):
        lang = data.split("::",1)[1]
        set_lang(chat_id, lang)
        bot.send_message(chat_id, t(chat_id, "lang_set"), reply_markup=main_menu_kb(chat_id))

    try:
        bot.answer_callback_query(call.id)
    except Exception:
        pass

@bot.message_handler(func=lambda m: True, content_types=['text'])
def on_text(message):
    chat_id = message.chat.id
    text = (message.text or "").strip()

    if chat_id in awaiting_query:
        awaiting_query.discard(chat_id)
        link = build_affiliate_link(text)
        bot.send_message(chat_id, f"Вот что нашёл по запросу «{text}»:\n\n🔗 {link}\n\n(демо; позже добавим карточки с фото)")
        return

    if chat_id in awaiting_track:
        awaiting_track.discard(chat_id)
        bot.send_message(chat_id, t(chat_id, "tracking_saved"))
        return

    bot.send_message(chat_id, t(chat_id, "unknown"), reply_markup=main_menu_kb(chat_id))

if __name__ == "__main__":
    print("Bot started.")
    bot.infinity_polling(skip_pending=True)
