import telebot

bot = telebot.TeleBot('Your telegram bot token')

@bot.message_handler(commands=['start'])
def pin(message):
    bot.send_message(message.chat.id, 'In the pinned message, all the mathematical signs that the bot can solve')
    pinn = bot.send_message(message.chat.id, 'x 1 numb, a 2 numb\n x+a addition\n x-a subtraction\n x*a multiplication\n x/a division\n x^a degree\n (x∛) cube root\n (x√) Square root\n () a priority').message_id
    bot.pin_chat_message(message.chat.id, message_id = pinn)

