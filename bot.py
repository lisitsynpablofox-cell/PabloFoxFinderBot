
import telebot
from telebot import types

# ================== CONFIG ==================
TOKEN = "8151618151:AAGVew78XfC1p4oa4fnVV5U0yQI0Fh9ygB0"  # WARNING: rotate later & move to env var BOT_TOKEN
DEFAULT_LANG = "ru"
# ===========================================

bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")
user_lang = {}

def t(uid: int, key: str) -> str:
    lang = user_lang.get(uid, DEFAULT_LANG)
    return TEXTS.get(lang, TEXTS["en"]).get(key, key)

TEXTS = {
    "ru": {
        "start": "👋 Привет! Я *PabloFoxFinderBot* — твой помощник по выгодным находкам.",
        "menu": "Главное меню:",
        "btn_find": "🔎 Поиск",
        "btn_categories": "🗂 Категории",
        "btn_track": "⏰ Трекинг цен",
        "btn_lang": "🌐 Язык",
        "find_hint": "Напиши, что ищем (например: *iPhone 15*).",
        "tracking_saved": "✅ Принял! Я запомнил запрос: *{q}*.",
        "choose_lang": "Выбери язык:",
        "lang_changed": "✅ Язык переключен на: *{lang}*",
        "unknown_lang": "❌ Неизвестный язык. Доступно: *ru, en, es, pt, fr, de, it*.",
        "choose_category": "Выбери категорию:",
        "cat_electronics": "📱 Электроника",
        "cat_home": "🏠 Дом и сад",
        "cat_fashion": "👗 Одежда",
        "cat_beauty": "💄 Красота",
        "cat_auto": "🚗 Авто",
        "echo_query": "Ищу: *{q}* (демо-ответ)\nСкоро подключим реальные офферы 😉",
        "help": "Команды:\n/start — меню\n/find — поиск\n/lang <ru|en|es|pt|fr|de|it> — язык",
    },
    "en": {
        "start": "👋 Hello! I’m *PabloFoxFinderBot* — your helper for great deals.",
        "menu": "Main menu:",
        "btn_find": "🔎 Find",
        "btn_categories": "🗂 Categories",
        "btn_track": "⏰ Price tracking",
        "btn_lang": "🌐 Language",
        "find_hint": "Type what we’re looking for (e.g., *iPhone 15*).",
        "tracking_saved": "✅ Got it! Saved your query: *{q}*.",
        "choose_lang": "Choose a language:",
        "lang_changed": "✅ Language switched to: *{lang}*",
        "unknown_lang": "❌ Unknown language. Available: *ru, en, es, pt, fr, de, it*.",
        "choose_category": "Choose a category:",
        "cat_electronics": "📱 Electronics",
        "cat_home": "🏠 Home & Garden",
        "cat_fashion": "👗 Fashion",
        "cat_beauty": "💄 Beauty",
        "cat_auto": "🚗 Auto",
        "echo_query": "Searching for: *{q}* (demo response)\nReal offers coming soon 😉",
        "help": "Commands:\n/start — menu\n/find — search\n/lang <ru|en|es|pt|fr|de|it> — language",
    },
    "es": {
        "start": "👋 ¡Hola! Soy *PabloFoxFinderBot* — tu ayudante para encontrar las mejores ofertas.",
        "menu": "Menú principal:",
        "btn_find": "🔎 Buscar",
        "btn_categories": "🗂 Categorías",
        "btn_track": "⏰ Seguimiento de precios",
        "btn_lang": "🌐 Idioma",
        "find_hint": "Escribe lo que buscas (p. ej., *iPhone 15*).",
        "tracking_saved": "✅ ¡Hecho! Guardé tu búsqueda: *{q}*.",
        "choose_lang": "Elige un idioma:",
        "lang_changed": "✅ Idioma cambiado a: *{lang}*",
        "unknown_lang": "❌ Idioma desconocido. Disponible: *ru, en, es, pt, fr, de, it*.",
        "choose_category": "Elige una categoría:",
        "cat_electronics": "📱 Electrónica",
        "cat_home": "🏠 Hogar y jardín",
        "cat_fashion": "👗 Moda",
        "cat_beauty": "💄 Belleza",
        "cat_auto": "🚗 Auto",
        "echo_query": "Buscando: *{q}* (respuesta demo)\nPronto añadiremos ofertas reales 😉",
        "help": "Comandos:\n/start — menú\n/find — buscar\n/lang <ru|en|es|pt|fr|de|it> — idioma",
    },
    "pt": {
        "start": "👋 Olá! Eu sou o *PabloFoxFinderBot* — seu ajudante para encontrar as melhores ofertas.",
        "menu": "Menu principal:",
        "btn_find": "🔎 Buscar",
        "btn_categories": "🗂 Categorias",
        "btn_track": "⏰ Acompanhar preços",
        "btn_lang": "🌐 Idioma",
        "find_hint": "Digite o que quer procurar (ex.: *iPhone 15*).",
        "tracking_saved": "✅ Pronto! Salvei sua busca: *{q}*.",
        "choose_lang": "Escolha um idioma:",
        "lang_changed": "✅ Idioma alterado para: *{lang}*",
        "unknown_lang": "❌ Idioma desconhecido. Disponível: *ru, en, es, pt, fr, de, it*.",
        "choose_category": "Escolha uma categoria:",
        "cat_electronics": "📱 Eletrônicos",
        "cat_home": "🏠 Casa e jardim",
        "cat_fashion": "👗 Moda",
        "cat_beauty": "💄 Beleza",
        "cat_auto": "🚗 Auto",
        "echo_query": "Procurando por: *{q}* (resposta demo)\nOfertas reais em breve 😉",
        "help": "Comandos:\n/start — menu\n/find — buscar\n/lang <ru|en|es|pt|fr|de|it> — idioma",
    },
    "fr": {
        "start": "👋 Salut ! Je suis *PabloFoxFinderBot* — ton aide pour dénicher les meilleurs bons plans.",
        "menu": "Menu principal :",
        "btn_find": "🔎 Rechercher",
        "btn_categories": "🗂 Catégories",
        "btn_track": "⏰ Suivi des prix",
        "btn_lang": "🌐 Langue",
        "find_hint": "Écris ce que tu cherches (ex. : *iPhone 15*).",
        "tracking_saved": "✅ C’est noté ! J’ai enregistré ta recherche : *{q}*.",
        "choose_lang": "Choisis une langue :",
        "lang_changed": "✅ Langue changée en : *{lang}*",
        "unknown_lang": "❌ Langue inconnue. Dispo : *ru, en, es, pt, fr, de, it*.",
        "choose_category": "Choisis une catégorie :",
        "cat_electronics": "📱 Électronique",
        "cat_home": "🏠 Maison & jardin",
        "cat_fashion": "👗 Mode",
        "cat_beauty": "💄 Beauté",
        "cat_auto": "🚗 Auto",
        "echo_query": "Recherche : *{q}* (réponse démo)\nDe vraies offres arrivent 😉",
        "help": "Commandes :\n/start — menu\n/find — recherche\n/lang <ru|en|es|pt|fr|de|it> — langue",
    },
    "de": {
        "start": "👋 Hallo! Ich bin *PabloFoxFinderBot* — dein Helfer für Top-Angebote.",
        "menu": "Hauptmenü:",
        "btn_find": "🔎 Suchen",
        "btn_categories": "🗂 Kategorien",
        "btn_track": "⏰ Preisüberwachung",
        "btn_lang": "🌐 Sprache",
        "find_hint": "Schreibe, wonach wir suchen (z. B. *iPhone 15*).",
        "tracking_saved": "✅ Alles klar! Ich habe deine Suche gespeichert: *{q}*.",
        "choose_lang": "Wähle eine Sprache:",
        "lang_changed": "✅ Sprache gewechselt zu: *{lang}*",
        "unknown_lang": "❌ Unbekannte Sprache. Verfügbar: *ru, en, es, pt, fr, de, it*.",
        "choose_category": "Wähle eine Kategorie:",
        "cat_electronics": "📱 Elektronik",
        "cat_home": "🏠 Haus & Garten",
        "cat_fashion": "👗 Mode",
        "cat_beauty": "💄 Beauty",
        "cat_auto": "🚗 Auto",
        "echo_query": "Suche nach: *{q}* (Demo-Antwort)\nEchte Angebote kommen bald 😉",
        "help": "Befehle:\n/start — Menü\n/find — Suche\n/lang <ru|en|es|pt|fr|de|it> — Sprache",
    },
    "it": {
        "start": "👋 Ciao! Sono *PabloFoxFinderBot* — il tuo aiuto per le migliori offerte.",
        "menu": "Menu principale:",
        "btn_find": "🔎 Cerca",
        "btn_categories": "🗂 Categorie",
        "btn_track": "⏰ Monitoraggio prezzi",
        "btn_lang": "🌐 Lingua",
        "find_hint": "Scrivi cosa cerchiamo (es.: *iPhone 15*).",
        "tracking_saved": "✅ Fatto! Ho salvato la tua ricerca: *{q}*.",
        "choose_lang": "Scegli una lingua:",
        "lang_changed": "✅ Lingua cambiata in: *{lang}*",
        "unknown_lang": "❌ Lingua sconosciuta. Disponibili: *ru, en, es, pt, fr, de, it*.",
        "choose_category": "Scegli una categoria:",
        "cat_electronics": "📱 Elettronica",
        "cat_home": "🏠 Casa & giardino",
        "cat_fashion": "👗 Moda",
        "cat_beauty": "💄 Bellezza",
        "cat_auto": "🚗 Auto",
        "echo_query": "Cerco: *{q}* (risposta demo)\nA breve offerte reali 😉",
        "help": "Comandi:\n/start — menu\n/find — cerca\n/lang <ru|en|es|pt|fr|de|it> — lingua",
    },
}

def make_menu(uid):
    lang = user_lang.get(uid, DEFAULT_LANG)
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton(TEXTS[lang]["btn_find"]), types.KeyboardButton(TEXTS[lang]["btn_categories"]))
    kb.add(types.KeyboardButton(TEXTS[lang]["btn_track"]), types.KeyboardButton(TEXTS[lang]["btn_lang"]))
    return kb

@bot.message_handler(commands=['start', 'help'])
def cmd_start(message):
    uid = message.from_user.id
    bot.send_message(uid, t(uid, "start"))
    bot.send_message(uid, t(uid, "menu"), reply_markup=make_menu(uid))

@bot.message_handler(commands=['lang'])
def cmd_lang(message):
    uid = message.from_user.id
    parts = message.text.split(maxsplit=1)
    if len(parts) == 2:
        lang = parts[1].lower()
        if lang in TEXTS:
            user_lang[uid] = lang
            bot.send_message(uid, t(uid, "lang_changed").format(lang=lang), reply_markup=make_menu(uid))
        else:
            bot.send_message(uid, t(uid, "unknown_lang"))
    else:
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton("Русский 🇷🇺", callback_data="lang:ru"),
               types.InlineKeyboardButton("English 🇬🇧", callback_data="lang:en"))
        kb.add(types.InlineKeyboardButton("Español 🇪🇸", callback_data="lang:es"),
               types.InlineKeyboardButton("Português 🇵🇹", callback_data="lang:pt"))
        kb.add(types.InlineKeyboardButton("Français 🇫🇷", callback_data="lang:fr"),
               types.InlineKeyboardButton("Deutsch 🇩🇪", callback_data="lang:de"))
        kb.add(types.InlineKeyboardButton("Italiano 🇮🇹", callback_data="lang:it"))
        bot.send_message(uid, t(uid, "choose_lang"), reply_markup=kb)

@bot.callback_query_handler(func=lambda c: c.data.startswith("lang:"))
def cb_lang(call):
    uid = call.from_user.id
    lang = call.data.split(":", 1)[1]
    if lang in TEXTS:
        user_lang[uid] = lang
        try:
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        except Exception:
            pass
        bot.answer_callback_query(call.id)
        bot.send_message(uid, t(uid, "lang_changed").format(lang=lang), reply_markup=make_menu(uid))
    else:
        bot.answer_callback_query(call.id, t(uid, "unknown_lang"), show_alert=True)

@bot.message_handler(func=lambda m: m.text in [TEXTS[x]["btn_find"] for x in TEXTS])
def btn_find(message):
    uid = message.from_user.id
    bot.send_message(uid, t(uid, "find_hint"))

@bot.message_handler(func=lambda m: m.text in [TEXTS[x]["btn_categories"] for x in TEXTS])
def btn_categories(message):
    uid = message.from_user.id
    lang = user_lang.get(uid, DEFAULT_LANG)
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(
        types.InlineKeyboardButton(TEXTS[lang]["cat_electronics"], callback_data="cat:electronics"),
        types.InlineKeyboardButton(TEXTS[lang]["cat_home"], callback_data="cat:home"),
        types.InlineKeyboardButton(TEXTS[lang]["cat_fashion"], callback_data="cat:fashion"),
        types.InlineKeyboardButton(TEXTS[lang]["cat_beauty"], callback_data="cat:beauty"),
        types.InlineKeyboardButton(TEXTS[lang]["cat_auto"], callback_data="cat:auto"),
    )
    bot.send_message(uid, t(uid, "choose_category"), reply_markup=kb)

@bot.callback_query_handler(func=lambda c: c.data.startswith("cat:"))
def cb_category(call):
    uid = call.from_user.id
    q = call.data.split(":", 1)[1]
    bot.answer_callback_query(call.id)
    bot.send_message(uid, t(uid, "echo_query").format(q=q))

@bot.message_handler(func=lambda m: m.text in [TEXTS[x]["btn_track"] for x in TEXTS])
def btn_track(message):
    uid = message.from_user.id
    bot.send_message(uid, t(uid, "find_hint"))

@bot.message_handler(content_types=['text'])
def handle_text(message):
    uid = message.from_user.id
    q = (message.text or "").strip()
    # Ignore service labels if they arrive as text
    service = [TEXTS[x]["btn_find"] for x in TEXTS] + [TEXTS[x]["btn_categories"] for x in TEXTS] + [TEXTS[x]["btn_track"] for x in TEXTS] + [TEXTS[x]["btn_lang"] for x in TEXTS]
    if q in service or q.startswith("/"):
        return
    if q:
        bot.send_message(uid, t(uid, "echo_query").format(q=q))

if __name__ == "__main__":
    print("Multilang bot started.")
    bot.infinity_polling(skip_pending=True, timeout=20)
