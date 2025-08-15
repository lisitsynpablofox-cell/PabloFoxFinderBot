# bot.py
import os
import time
import logging
from urllib.parse import quote_plus
import telebot
from telebot import types, util

# ====== CONFIG ======
TOKEN = os.environ.get("TOKEN")  # на Render переменная TOKEN уже есть
DEFAULT_LANG = "ru"
# ====================

if not TOKEN:
    raise RuntimeError("Environment variable TOKEN is not set. Add it in Render → Environment as TOKEN.")

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")

# --------- i18n texts ---------
TEXTS = {
    "ru": {
        "start": "👋 Привет! Я *PabloFoxFinderBot* — твой помощник по выгодным находкам.",
        "menu": "Главное меню:",
        "btn_find": "🔎 Поиск",
        "btn_categories": "🗂 Категории",
        "btn_track": "⏰ Трекинг цен",
        "btn_lang": "🌐 Язык",
        "find_hint": "Напиши, что ищем (например: *iPhone 15*). Я пришлю ссылки с трекингом на магазины.",
        "choose_lang": "Выбери язык:",
        "lang_changed": "✅ Язык переключен на: *{lang}*",
        "unknown_lang": "❌ Неизвестный язык. Доступно: ru, en, es, pt, fr, de, it.",
        "choose_category": "Выбери категорию:",
        "cat_electronics": "📱 Электроника",
        "cat_home": "🏠 Дом и сад",
        "cat_fashion": "👗 Одежда",
        "cat_beauty": "💄 Красота",
        "cat_auto": "🚗 Авто",
        "search_result": "Вот ссылки по запросу «*{q}*»:",
        "help": "Команды:\n/start — меню\n/find — поиск\n/lang ru|en|es|pt|fr|de|it — язык",
    },
    "en": {
        "start": "👋 Hey! I’m *PabloFoxFinderBot* — your helper for great deals.",
        "menu": "Main menu:",
        "btn_find": "🔎 Find",
        "btn_categories": "🗂 Categories",
        "btn_track": "⏰ Price tracking",
        "btn_lang": "🌐 Language",
        "find_hint": "Type what to search (e.g., *iPhone 15*). I’ll send tracked store links.",
        "choose_lang": "Choose a language:",
        "lang_changed": "✅ Language switched to: *{lang}*",
        "unknown_lang": "❌ Unknown language. Available: ru, en, es, pt, fr, de, it.",
        "choose_category": "Choose a category:",
        "cat_electronics": "📱 Electronics",
        "cat_home": "🏠 Home & Garden",
        "cat_fashion": "👗 Fashion",
        "cat_beauty": "💄 Beauty",
        "cat_auto": "🚗 Auto",
        "search_result": "Here are links for “*{q}*”:",
        "help": "Commands:\n/start — menu\n/find — search\n/lang ru|en|es|pt|fr|de|it — language",
    },
    "es": {
        "start": "👋 ¡Hola! Soy *PabloFoxFinderBot* — tu ayuda para conseguir ofertas.",
        "menu": "Menú principal:",
        "btn_find": "🔎 Buscar",
        "btn_categories": "🗂 Categorías",
        "btn_track": "⏰ Seguimiento de precios",
        "btn_lang": "🌐 Idioma",
        "find_hint": "Escribe qué buscas (p. ej., *iPhone 15*). Enviaré enlaces con tracking.",
        "choose_lang": "Elige un idioma:",
        "lang_changed": "✅ Idioma cambiado a: *{lang}*",
        "unknown_lang": "❌ Idioma desconocido. Disponible: ru, en, es, pt, fr, de, it.",
        "choose_category": "Elige una categoría:",
        "cat_electronics": "📱 Electrónica",
        "cat_home": "🏠 Hogar y jardín",
        "cat_fashion": "👗 Moda",
        "cat_beauty": "💄 Belleza",
        "cat_auto": "🚗 Auto",
        "search_result": "Enlaces para “*{q}*”:",
        "help": "Comandos:\n/start — menú\n/find — buscar\n/lang ru|en|es|pt|fr|de|it — idioma",
    },
    "pt": {
        "start": "👋 Olá! Eu sou o *PabloFoxFinderBot* — seu ajudante para ofertas.",
        "menu": "Menu principal:",
        "btn_find": "🔎 Buscar",
        "btn_categories": "🗂 Categorias",
        "btn_track": "⏰ Acompanhar preços",
        "btn_lang": "🌐 Idioma",
        "find_hint": "Digite o que deseja procurar (ex.: *iPhone 15*). Enviarei links com tracking.",
        "choose_lang": "Escolha um idioma:",
        "lang_changed": "✅ Idioma alterado para: *{lang}*",
        "unknown_lang": "❌ Idioma desconhecido. Disponível: ru, en, es, pt, fr, de, it.",
        "choose_category": "Escolha uma categoria:",
        "cat_electronics": "📱 Eletrônicos",
        "cat_home": "🏠 Casa e jardim",
        "cat_fashion": "👗 Moda",
        "cat_beauty": "💄 Beleza",
        "cat_auto": "🚗 Auto",
        "search_result": "Links para “*{q}*”:",
        "help": "Comandos:\n/start — menu\n/find — buscar\n/lang ru|en|es|pt|fr|de|it — idioma",
    },
    "fr": {
        "start": "👋 Salut ! Je suis *PabloFoxFinderBot* — ton aide pour de bons plans.",
        "menu": "Menu principal :",
        "btn_find": "🔎 Rechercher",
        "btn_categories": "🗂 Catégories",
        "btn_track": "⏰ Suivi des prix",
        "btn_lang": "🌐 Langue",
        "find_hint": "Écris ce que tu cherches (ex. : *iPhone 15*). J’enverrai des liens tracés.",
        "choose_lang": "Choisis une langue :",
        "lang_changed": "✅ Langue changée en : *{lang}*",
        "unknown_lang": "❌ Langue inconnue. Dispo : ru, en, es, pt, fr, de, it.",
        "choose_category": "Choisis une catégorie :",
        "cat_electronics": "📱 Électronique",
        "cat_home": "🏠 Maison & jardin",
        "cat_fashion": "👗 Mode",
        "cat_beauty": "💄 Beauté",
        "cat_auto": "🚗 Auto",
        "search_result": "Liens pour « *{q}* » :",
        "help": "Commandes :\n/start — menu\n/find — recherche\n/lang ru|en|es|pt|fr|de|it — langue",
    },
    "de": {
        "start": "👋 Hallo! Ich bin *PabloFoxFinderBot* — dein Helfer für Angebote.",
        "menu": "Hauptmenü:",
        "btn_find": "🔎 Suchen",
        "btn_categories": "🗂 Kategorien",
        "btn_track": "⏰ Preisüberwachung",
        "btn_lang": "🌐 Sprache",
        "find_hint": "Schreibe, wonach gesucht wird (z. B. *iPhone 15*). Ich sende getrackte Links.",
        "choose_lang": "Wähle eine Sprache:",
        "lang_changed": "✅ Sprache gewechselt zu: *{lang}*",
        "unknown_lang": "❌ Unbekannte Sprache. Verfügbar: ru, en, es, pt, fr, de, it.",
        "choose_category": "Wähle eine Kategorie:",
        "cat_electronics": "📱 Elektronik",
        "cat_home": "🏠 Haus & Garten",
        "cat_fashion": "👗 Mode",
        "cat_beauty": "💄 Beauty",
        "cat_auto": "🚗 Auto",
        "search_result": "Links für „*{q}*“:",
        "help": "Befehle:\n/start — Menü\n/find — Suche\n/lang ru|en|es|pt|fr|de|it — Sprache",
    },
    "it": {
        "start": "👋 Ciao! Sono *PabloFoxFinderBot* — il tuo aiuto per le offerte.",
        "menu": "Menu principale:",
        "btn_find": "🔎 Cerca",
        "btn_categories": "🗂 Categorie",
        "btn_track": "⏰ Monitoraggio prezzi",
        "btn_lang": "🌐 Lingua",
        "find_hint": "Scrivi cosa cercare (es.: *iPhone 15*). Invierò link tracciati.",
        "choose_lang": "Scegli una lingua:",
        "lang_changed": "✅ Lingua cambiata in: *{lang}*",
        "unknown_lang": "❌ Lingua sconosciuta. Disponibili: ru, en, es, pt, fr, de, it.",
        "choose_category": "Scegli una categoria:",
        "cat_electronics": "📱 Elettronica",
        "cat_home": "🏠 Casa & giardino",
        "cat_fashion": "👗 Moda",
        "cat_beauty": "💄 Bellezza",
        "cat_auto": "🚗 Auto",
        "search_result": "Link per “*{q}*”:",
        "help": "Comandi:\n/start — menu\n/find — cerca\n/lang ru|en|es|pt|fr|de|it — lingua",
    },
}

# простое хранение выбранного языка в памяти процесса
user_lang = {}
def get_lang(uid): return user_lang.get(uid, DEFAULT_LANG)
def t(uid, key): return TEXTS.get(get_lang(uid), TEXTS["en"]).get(key, key)

# ---------- affiliate links (заглушки PID/SUBID поправим позже) ----------
def link_aliexpress(q: str) -> str:
    return f"https://aliexpress.com/wholesale?SearchText={quote_plus(q)}&aff_platform=portals-tool&aff_fcid=DEMO"
def link_ozon(q: str) -> str:
    return f"https://www.ozon.ru/search/?text={quote_plus(q)}&from=affiliate_demo"
def link_wb(q: str) -> str:
    return f"https://www.wildberries.ru/catalog/0/search.aspx?search={quote_plus(q)}&aff=demo"

def stores_kb(q: str):
    kb = types.InlineKeyboardMarkup()
    kb.add(
        types.InlineKeyboardButton("AliExpress", url=link_aliexpress(q)),
        types.InlineKeyboardButton("Ozon", url=link_ozon(q)),
    )
    kb.add(types.InlineKeyboardButton("Wildberries", url=link_wb(q)))
    return kb

# ---------- keyboards ----------
def main_menu(uid):
    lang = get_lang(uid)
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(TEXTS[lang]["btn_find"], TEXTS[lang]["btn_categories"])
    kb.add(TEXTS[lang]["btn_track"], TEXTS[lang]["btn_lang"])
    return kb

def categories_inline(uid):
    lang = get_lang(uid)
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(
        types.InlineKeyboardButton(TEXTS[lang]["cat_electronics"], callback_data="cat:electronics"),
        types.InlineKeyboardButton(TEXTS[lang]["cat_home"], callback_data="cat:home"),
        types.InlineKeyboardButton(TEXTS[lang]["cat_fashion"], callback_data="cat:fashion"),
        types.InlineKeyboardButton(TEXTS[lang]["cat_beauty"], callback_data="cat:beauty"),
        types.InlineKeyboardButton(TEXTS[lang]["cat_auto"], callback_data="cat:auto"),
    )
    return kb

# ---------- commands ----------
@bot.message_handler(commands=["start", "help"])
def cmd_start(message):
    uid = message.from_user.id
    bot.send_message(uid, TEXTS[get_lang(uid)]["start"])
    bot.send_message(uid, TEXTS[get_lang(uid)]["menu"], reply_markup=main_menu(uid))

@bot.message_handler(commands=["lang"])
def cmd_lang(message):
    uid = message.from_user.id
    parts = message.text.split(maxsplit=1)
    if len(parts) == 2 and parts[1].lower() in TEXTS:
        user_lang[uid] = parts[1].lower()
        bot.send_message(uid, TEXTS[get_lang(uid)]["lang_changed"].format(lang=parts[1].lower()), reply_markup=main_menu(uid))
        return
    kb = types.InlineKeyboardMarkup()
    kb.add(
        types.InlineKeyboardButton("Русский 🇷🇺", callback_data="lang:ru"),
        types.InlineKeyboardButton("English 🇬🇧", callback_data="lang:en"),
    )
    kb.add(
        types.InlineKeyboardButton("Español 🇪🇸", callback_data="lang:es"),
        types.InlineKeyboardButton("Português 🇵🇹", callback_data="lang:pt"),
    )
    kb.add(
        types.InlineKeyboardButton("Français 🇫🇷", callback_data="lang:fr"),
        types.InlineKeyboardButton("Deutsch 🇩🇪", callback_data="lang:de"),
        types.InlineKeyboardButton("Italiano 🇮🇹", callback_data="lang:it"),
    )
    bot.send_message(uid, TEXTS[get_lang(uid)]["choose_lang"], reply_markup=kb)

@bot.callback_query_handler(func=lambda c: c.data.startswith("lang:"))
def cb_lang(call):
    uid = call.from_user.id
    lang = call.data.split(":",1)[1]
    if lang in TEXTS:
        user_lang[uid] = lang
        try:
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        except Exception:
            pass
        bot.answer_callback_query(call.id)
        bot.send_message(uid, TEXTS[get_lang(uid)]["lang_changed"].format(lang=lang), reply_markup=main_menu(uid))
    else:
        bot.answer_callback_query(call.id, TEXTS[get_lang(uid)]["unknown_lang"], show_alert=True)

@bot.message_handler(commands=["find"])
def cmd_find(message):
    uid = message.from_user.id
    bot.send_message(uid, TEXTS[get_lang(uid)]["find_hint"])

@bot.message_handler(func=lambda m: m.text in [TEXTS[x]["btn_categories"] for x in TEXTS])
def btn_categories(message):
    uid = message.from_user.id
    bot.send_message(uid, TEXTS[get_lang(uid)]["choose_category"], reply_markup=categories_inline(uid))

@bot.callback_query_handler(func=lambda c: c.data.startswith("cat:"))
def cb_cat(call):
    uid = call.from_user.id
    q = call.data.split(":",1)[1]
    bot.answer_callback_query(call.id)
    bot.send_message(uid, TEXTS[get_lang(uid)]["search_result"].format(q=q), reply_markup=stores_kb(q))

@bot.message_handler(func=lambda m: m.text in [TEXTS[x]["btn_find"] for x in TEXTS])
def btn_find(message):
    cmd_find(message)

@bot.message_handler(func=lambda m: m.text in [TEXTS[x]["btn_track"] for x in TEXTS])
def btn_track(message):
    uid = message.from_user.id
    bot.send_message(uid, TEXTS[get_lang(uid)]["find_hint"])

# универсальный обработчик текста — воспринимаем как поисковый запрос
@bot.message_handler(content_types=["text"])
def any_text(message):
    uid = message.from_user.id
    q = (message.text or "").strip()
    if not q or q.startswith("/"):
        return
    bot.send_message(uid, TEXTS[get_lang(uid)]["search_result"].format(q=q), reply_markup=stores_kb(q))

# устойчивый запуск long-polling
def run():
    # на всякий случай — снимаем вебхук (мы работаем через polling)
    try:
        bot.remove_webhook()
    except Exception as e:
        logging.warning("Webhook remove warning: %s", e)
    while True:
        try:
            logging.info("Starting polling…")
            bot.infinity_polling(skip_pending=True, timeout=60, long_polling_timeout=60, allowed_updates=util.update_types)
        except Exception as e:
            logging.exception("Polling crashed: %s", e)
            time.sleep(3)

if __name__ == "__main__":
    run()
