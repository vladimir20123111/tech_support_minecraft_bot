import telebot
from tech_support_minecraft_bot.config import BOT_TOKEN
bot = telebot.TeleBot(BOT_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "что вы хотите узнать? (бан, гайд)")

@bot.message_handler(func=lambda message: 'бан')
def handle_message(message):
    bot.reply_to(message, "что не так? (Почему забанели?, Куда делись все мой деньги после бана?, Что такое читы?, Что такое бан?, Можно поговорить с создателям?)")


@bot.message_handler(func=lambda message: 'Почему забанели?')
def handle_message(message):   
    bot.answer_callback_query(message.id, "Более вероятно, вы были заблакированы иза того что вы играли с читами которые запрещены в использование в том сервере в котором вы играли что даёт (срок) дней бана или за не хотения зделать проверку или за обзывание модераторов. Если не хотите ждать столько времени то можете купить разбан за (количество) рублей. Если читаете что вас забанели без причины то поимите, модератор снимают все проверки которве они делают и если вы не согласны с блакировкай то есть докозательство против вас")

@bot.message_handler(func=lambda message: 'Куда делись все мой деньги?')
def handle_message(message):   
    bot.answer_callback_query(message.id, "Деньги которые вы потратили не делись никуда, они до сих пор находятся в акаунте в котором вы играли до бана, так что мы не имее право вернуть вам деньги. Если не поняли то обясьню кратко. Вы купили майку в магазине, вам не понравилось и вы хотите те потраченые деньги не возврощая майку в замен.")

@bot.message_handler(func=lambda message: 'Что такое читы?')
def handle_message(message):   
    bot.answer_callback_query(message.id, "Читы это програма которая позволяет играть намного проще чем без них, пример в ревльной жизни: бесконечные деньги, уметь летать, телепортироватся и т.д.")

@bot.message_handler(func=lambda message: 'Что такое бан?')
def handle_message(message):   
    bot.answer_callback_query(message.id, "Бан это блокировка акаунта, проще говоря, запрет играть на сервере на кокоэта время")

@bot.message_handler(func=lambda message: 'Можно поговорить с создателям?')
def handle_message(message):   
    bot.answer_callback_query(message.id, "Можно, но более вероятно что создатель занят, так что если он не отвечает то надо подождать или пишите когда увидеш его в онлайне")

@bot.message_handler(func=lambda message: 'гайд')
def handle_message(message):
    bot.reply_to(message, "")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, "напишите ешё раз правильно, и с первой заглавной буквой")

bot.infinity_polling()