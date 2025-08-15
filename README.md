
# PabloFoxFinderBot (Ready-to-deploy)

Телеграм-бот с меню, поиском и категориями. Готов к деплою на Render.

## Как запустить локально
1. Python 3.9+
2. Установи зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Запусти с переменной окружения:
   ```bash
   export BOT_TOKEN="ВАШ_ТОКЕН_ОТ_BOTFATHER"
   python bot.py
   ```
   Windows PowerShell:
   ```powershell
   setx BOT_TOKEN "ВАШ_ТОКЕН_ОТ_BOTFATHER"
   python bot.py
   ```

## Деплой на Render (бесплатно)
1. Залей файлы в GitHub (bot.py, requirements.txt).
2. На https://render.com → New → Web Service.
3. Build Command:
   ```
   pip install -r requirements.txt
   ```
4. Start Command:
   ```
   python bot.py
   ```
5. Environment Variables:
   - `BOT_TOKEN` = токен из BotFather
   - (опц.) `DEFAULT_LANG` = ru|en

## Где править партнёрские ссылки
В `bot.py` функция `build_affiliate_link(query)` — туда подставь свои параметры (AliExpress PID/SUBID).
