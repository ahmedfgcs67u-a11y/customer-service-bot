import os
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMIN_ID = os.environ.get("ADMIN_ID")

if not BOT_TOKEN:
    raise ValueError("لم يتم توفير التوكن!")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "مرحباً بك! البوت يعمل بنجاح على السحابة على مدار الساعة.")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, f"وصلت رسالتك: {message.text}")

print("🚀 البوت قيد التشغيل السحابي...")
bot.infinity_polling()
