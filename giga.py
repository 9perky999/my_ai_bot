import telebot
from gigachat import GigaChat

# ВСТАВЬ СЮДА СВОИ КЛЮЧИ
TELEGRAM_TOKEN = "9087513004:AAEfw35GqnNCFrTL5kljrOiPjnVWYs62Moc"
GIGACHAT_KEY = "MDFhMWMwZDgtYTQxOC03NGQyLWFjZWUtMDc4ZDdiNTQ2NzNlOjlhMjFkNmEyLTkzM2QtNDdkZC04YzkyLTFlYWVjNmFhMzFjNQ=="

giga = GigaChat(
    credentials=GIGACHAT_KEY, 
    model="GigaChat-2", 
    scope="GIGACHAT_API_PERS", 
    verify_ssl_certs=False
)
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    # СЧЕТЧИК НОВЫХ ПОЛЬЗОВАТЕЛЕЙ
    print(f"🔥 Новый пользователь: ID {message.from_user.id}, Имя: {message.from_user.first_name}")
    
    text = (
        "Здарова, братан! Я твой умный ИИ-помощник. 🤖\n\n"
        "Спрашивай меня о чем угодно: помогу с домашкой, объясню сложное простыми словами или просто поболтаем. 😎\n\n"
        "👨‍💻 *Связь с владельцем:* /owner"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

@bot.message_handler(commands=['help', 'owner'])
def help_message(message):
    text = (
        "👨‍💻 *Связь с владельцем:*\n\n"
        "Если у тебя есть идеи, нашел баг или хочешь что-то предложить, "
        "пиши сюда 👉 https://t.me/anonaskbot?start=uxnlvsg"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    # СЧЕТЧИК СООБЩЕНИЙ
    print(f"💬 Сообщение от {message.from_user.first_name}: {message.text}")
    
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
