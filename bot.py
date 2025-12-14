from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = "8145844743:AAGI9XP7IeYJH-1-LVrPkYzmet5Hqyec--c"

WELCOME_MESSAGE = """
🤖 *Selamat Datang di Bot Resmi Kami!*

Halo 👋  
Terima kasih telah bergabung.

---

🎉 *Selamat Menikmati Layanan Kami*

Gunakan bot ini dengan bijak dan jangan lewatkan update penting yang akan kami kirimkan secara berkala.

---
LOCAL_BANNER = "banner.jpg"
🔗 *Link Penting*

🌐 GRUP TELEGRAM
👉 https://t.me/linkviralindoo

💬 CERITA DEWASA 
👉 https://emikoblue.com/

📢 CHANNEL BACKUP  
👉 https://t.me/viralteraboxhariini

🎰 LINK JP
👉 https://hokiku.link/Hoki89
"""

 try:
        with open(LOCAL_BANNER, "rb") as photo:
            await update.message.reply_photo(photo=photo, caption=caption, parse_mode="Markdown", reply_markup=reply_markup)
    except FileNotFoundError:
        await update.message.reply_photo(photo=LOCAL_BANNER, caption=caption, parse_mode="Markdown", reply_markup=reply_markup)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        WELCOME_MESSAGE,
        parse_mode="Markdown",
        disable_web_page_preview=True
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 Bot berjalan...")
    app.run_polling()

if __name__ == "__main__":
    main()
