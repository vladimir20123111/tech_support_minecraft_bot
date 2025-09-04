import telebot
from config import BOT_TOKEN
bot = telebot.TeleBot(BOT_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "какая у вас причина? (бан, вернуть денги за покупку в сервере)")

@bot.message_handler(func=lambda message: 'бан')
def handle_message(message):   
    bot.answer_callback_query(message.id, "более вероятно, вы были забанены иза того что вы играли с читами что даёт (срок) дней бана или за не хотения зделать проверку или за обзывание модераторов. Если не хотите ждать столько времени то можете купить разбан за (количество) рублей. Если читаете что вас забанели без причины то поимите, модератор снимают все проверки и если вы не согласны с баном то есть докозательство против вас")

@bot.message_handler(func=lambda message: 'вернуть денги за покупку в сервере')
def handle_message(message):   
    bot.answer_callback_query(message.id, "")

bot.infinity_polling()