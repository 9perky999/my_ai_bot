


import telebot
from gigachat import GigaChat

# ТВОИ КЛЮЧИ (я вставил те, что были на скрине, но проверь!)
TELEGRAM_TOKEN = "9087513004:AAHDykShzFdWCZ7VBLhjfYQ1NGGjihGVfNU"
GIGACHAT_KEY = "MDFhMWMwZDgtYTQxOC03NGQyLWFjZWUtMDc4ZDdiNTQ2NzNlOmVhNmE5Y2RjLWEwNWQtNDQ5Ni04YWMxLTlhNDFjNmMzMTFmZg=="

# Подключение к GigaChat с указанием модели
giga = GigaChat(credentials=GIGACHAT_KEY, model="GigaChat-2", verify_ssl_certs=False)

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я твой умный ИИ-помощник. Напиши мне любой вопрос, и я отвечу! 😎")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_chat_action(message.chat.id, 'typing')
    try:
        # Отправляем запрос в нейросеть
        response = giga.chat(message.text)
        answer = response.choices[0].message.content
        
        # Убираем доллары и слэши из ответа (чтобы не было формул)
        answer = answer.replace("$", "").replace("\\", "")
        
        bot.reply_to(message, answer)
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")

print("ИИ-бот запущен!")
bot.infinity_polling()
