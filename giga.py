import telebot
from gigachat import GigaChat

# ТВОИ КЛЮЧИ
TELEGRAM_TOKEN= "9087513004:AAEfw35GqnNCFrTL5kljrOiPjnVWYs62Moc"
GIGACHAT_KEY = "MDFhMWMwZDgtYTQxOC03NGQyLWFjZWUtMDc4ZDdiNTQ2NzNlOjZiMmM2NjcxLWI3MzQtNGYzOC1hZWIzLTBiYjdjZTQxOWE3Nw=="

giga = GigaChat(credentials=GIGACHAT_KEY, model="GigaChat-2", verify_ssl_certs=False)
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    text = (
        "Здарова, братан! Я твой умный ИИ-помощник. 🤖\n\n"
        "Спрашивай меня о чем угодно: помогу с домашкой, объясню сложное простыми словами или просто поболтаем. 😎\n\n"
        "👨‍💻 *Связь с владельцем:*/owner"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

@bot.message_handler(commands=['help', 'owner'])
def help_message(message):
    # ТУТ МОЖЕШЬ ВСТАВИТЬ СВОЮ ССЫЛКУ НА АНОНИМНОГО БОТА ВМЕСТО t.me/anonaskbot?start=uxn1vsg
    text = (
        "👨‍💻 *Связь с владельцем:*\n\n"
        "Если у тебя есть идеи, нашел баг или хочешь что-то предложить, "
        "пиши сюда 👉 t.me/anonaskbot?start=uxn1vsg\n\n"
        
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_chat_action(message.chat.id, 'typing')
    try:
        messages = [
            {
                "role": "system", 
                "content": "Ты обычный пацан-помощник. Отвечай простым русским языком. Если тебя просят решить математический пример, пиши сразу только итоговый ответ цифрами (например: 150). НИКОГДА не пиши слова times, multiplied by, формулы, знаки $ и обратные слэши."
            },
            {
                "role": "user", 
                "content": message.text
            }
        ]
        
        response = giga.chat({"messages": messages})
        answer = response.choices[0].message.content
        
        answer = answer.replace("$", "").replace("\\", "").replace("times", "*")
        
        bot.reply_to(message, answer)
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")

print("ИИ-бот запущен!")
bot.infinity_polling()
