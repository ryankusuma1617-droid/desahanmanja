from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "8145844743:AAGI9XP7IeYJH-1-LVrPkYzmet5Hqyec--c"

LOCAL_BANNER = "banner.png"
DOWNLOAD_APK_URL = "https://t.me/viralteraboxhariini"
LINK_ALT_1 = "https://t.me/linkviralindoo"
LINK_ALT_2 = "https://t.me/linkviralindoo"
RTP_GACOR_URL = "https://emikoblue.com/"
CONTACT_TELEGRAM = "https://hokiku.link/Hoki89"
CONTACT_WHATSAPP = "https://hokiku.link/Hoki89"
CONTACT_LIVECHAT = "https://hokiku.link/Hoki89"

async def start(update: Update, context) -> None:
    caption = (
        "👑 Selamat Datang Di Situs Desahan Manja 👑\n\n"
        
    )

    keyboard = [
        [
            KeyboardButton("💋 GRUP TELEGRAM"),
            KeyboardButton("🫦 CERITA DEWASA"),
        ],
        [
            KeyboardButton("📱 CHANNEL BACKUP"),
            KeyboardButton("🌐 LINK JP"),
        ]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    try:
        with open(LOCAL_BANNER, "rb") as photo:
            await update.message.reply_photo(photo=photo, caption=caption, parse_mode="Markdown", reply_markup=reply_markup)
    except FileNotFoundError:
        await update.message.reply_photo(photo=LOCAL_BANNER, caption=caption, parse_mode="Markdown", reply_markup=reply_markup)

async def button_callback(update: Update, context) -> None:
    text = update.message.text

    if text == "💋 GRUP TELEGRAM":
        reply = (
            "🌐 *👑 Selamat Datang Di Situs Desahan Manja 👑*\n\n"
        )
        keyboard = [
            [
                InlineKeyboardButton("💋 Link 1", url=LINK_ALT_1),
                InlineKeyboardButton("💋 Link 2", url=LINK_ALT_2)
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(reply, parse_mode="Markdown", reply_markup=reply_markup)

    elif text == "🫦 CERITA DEWASA":
        reply = (
            "🫦 *👑 Selamat Datang Di Situs Desahan Manja 👑*\n\n"
        )
        keyboard = [
            [
                InlineKeyboardButton("💋 LINK", url=RTP_GACOR_URL),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(reply, parse_mode="Markdown", reply_markup=reply_markup)

    elif text == "📱 CHANNEL BACKUP":
        reply = (
            "📱 *DOWNLOAD APLIKASI KAMI UNTUK BERMAIN DENGAN MUDAH SETIAP HARI*\n\n"
        )
        keyboard = [
            [
                InlineKeyboardButton("💋 LINK", url=DOWNLOAD_APK_URL),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(reply, parse_mode="Markdown", reply_markup=reply_markup)

    elif text == "🌐 LINK JP":
        reply = (
            "☎️ *HUBUNGI ADMIN DESAHAN MANJA DENGAN PELAYANAN ONLINE 24 JAM*\n\n"
        )
        keyboard = [
            [
                InlineKeyboardButton("📱 LINK", url=CONTACT_TELEGRAM),
            ],
            [
                InlineKeyboardButton("📩 LINK", url=CONTACT_WHATSAPP),
            ],
            [
                InlineKeyboardButton("💬 LINK", url=CONTACT_LIVECHAT),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(reply, parse_mode="Markdown", reply_markup=reply_markup)

    else:
        reply = "⚠️ Silahkan Pilih Menu Yang Tersedia."
        await update.message.reply_text(reply, parse_mode="Markdown")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, button_callback))

    print("🤖 Bot DESAHAN MANJA is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
